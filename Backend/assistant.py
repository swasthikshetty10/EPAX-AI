from nltk.stem import WordNetLemmatizer
import nltk
import os
from os.path import join
import smtplib
from urllib.request import urlopen
import json
import numpy as np
from pyjokes import jokes_de
import tensorflow
from tensorflow import keras
import pickle
#from googletrans import Translator
import random
from tensorflow.keras.models import load_model
#### importing functions ####
from Backend.AssistantFunctions import codehelp, note_taking, questions, jokes, rps, whatis, news, database, pymemes, translate__
#translator = Translator()
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


model = load_model('Trained_Models/bot.h5')
intents = json.loads(open('Trained_Models/intents.json').read())
words = pickle.load(open('Trained_Models/words.pkl', 'rb'))
classes = pickle.load(open('Trained_Models/classes.pkl', 'rb'))
#### Predictions  ################
####################################
#######################################


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return(np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.9
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    # print(results)
    return_list = []
#     for r in results:
#         return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    try:
        if results[0]:
            for r in results:
                return_list.append(
                    {"intent": classes[r[0]], "probability": str(r[1])})
        else:
            return_list.append({"intent": 'noanswer', "probability": '1'})
    except:
        return_list.append({"intent": 'noanswer', "probability": '1'})
    # print(return_list)
    return return_list


def getResponse(ints, intents_json):
    result = 'sorry i could not understand'
    tag = ints[0]['intent']
    # print(tag)
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result, tag


def prediction(msg):
    ints = predict_class(msg, model)
    res, tag = getResponse(ints, intents)
    if float(ints[0]['probability']) > 0.95:
        result = {"response": res,
                  "tag": tag
                  }
    else:
        result = {"response": "sorry i could not understand what you are saying",
                  "tag": "couldnotunderstand"
                  }

    return result
# text to response


def to_json(response, tag=None, Notes=None, urls=None,):
    stuf_for_frontend = {
        "response": response,
        "tag": tag,
        "notes": Notes,
        "urls": urls,
    }

    return stuf_for_frontend


# taking command from response
def takeCommand(cmd):

    return cmd


# # predicting solution from machine learning model
# def prediction(query):
#     intents = None
#     with open("Backend/intents.json") as file:
#         data = json.load(file)
#     model = keras.models.load_model('chat_model')
#     with open('Backend/tokenizer.pickle', 'rb') as handle:
#         tokenizer = pickle.load(handle)
#     with open('Backend/label_encoder.pickle', 'rb') as enc:
#         lbl_encoder = pickle.load(enc)
#     max_len = 20
#     result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([query]),
#                                                                       truncating='post', maxlen=max_len))
#     # print(tensorflow.Tensor(result))
#     # print(np.max(result))
#     tag = lbl_encoder.inverse_transform([np.argmax(result)])
#     for i in data['intents']:
#         if i['tag'] == tag:
#             intents = to_json(response=np.random.choice(
#                 i['responses']), tag=str(tag))
#     return intents


def clear(): return os.system('cls')


clear()


# opening intents
with open("Trained_Models/intents.json") as file:
    data = json.load(file)


def converttostring(list):

    res = str(", ".join(map(str, list)))

    return res


# saving question pattrens for cross checking
mlquestions = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        if 'what is' in pattern or 'who is' in pattern:
            mlquestions.append(pattern)

howdo = [
    "how do",
    "how to",
]

# main


def sendnotes(notes):
    try:
        usr_id = notes['id']
        title = notes['title']
        notes = notes['notes']
        note_taking.add_note(id_=usr_id, title=title, note=notes)
        return True
    except Exception as e:
        # print(e)
        return False


def deletenotes(notes):
    try:
        usr_id = notes['id']
        title = notes['title']

        note_taking.del_note(usr_id, title)
        return True
    except:
        return False


def noteslist(usr_id):
    try:

        allnotes = note_taking.list_notes(id_=usr_id)
        return allnotes
    except:
        return False


def readnotes(usr_id, title):
    try:
        notes = note_taking.list_notes(id_=usr_id)

        return notes[title]
    except Exception as e:
        print(e)
        return False


def getjokes():
    return jokes.pyjoke()


def get_meme():
    memes = pymemes.get_meme('ProgrammerHumor')
    return random.choice(memes)


##### response #####

def miku_speak(query):

    # if query != 'none':
    #     obj = translator.translate(query)
    #     query = obj.text
    #     print(query)
    stuff_for_frontend = None
    if query != 'none':
        # search google and wolfarm alpha ,
        if ('what is' in query or 'where is' in query or 'which is' in query or 'who is' in query) and query not in mlquestions:
            try:
                stuff_for_frontend = to_json(
                    response=questions.askquest(question=query), tag="questions")
            except:
                try:
                    stuff_for_frontend = to_json(response=whatis.wiki(
                        query=query)['summary'], tag="wikipedia")
                except:
                    stuff_for_frontend = to_json(
                        response='i found this on web', tag="epaxsearch", urls=query)

        elif any(x in query for x in howdo):
            stuff_for_frontend = to_json(
                response="I found these on web", tag="epaxsearch", urls=query)
        elif "search" in query[:13]:
            query = query.replace("search", "")
            stuff_for_frontend = to_json(
                response="I found these on web", tag="epaxsearch", urls=query)
        elif 'translate' in query:
            try:
                __query = query.replace("translate", "")
                # print(__query)
                response_ = translate__.gtranslate(query=__query)
                print(response_)
                stuff_for_frontend = to_json(
                    response=response_, tag="translate")
            except Exception as e:
                print(e)
                stuff_for_frontend = to_json(
                    response="sorry could not translate", tag="translate")

        else:

            #print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
            try:

                stuff_for_frontend = prediction(query)
                tag = stuff_for_frontend.get('tag')
                # open stack overflow
                if tag == 'stackoverflow':

                    stuff_for_frontend = to_json(
                        response='oh but i cant fix your error right now')

                # create notes
                # if tag == 'note-taking':
                #     title = input('Title :')
                #     notes = input('type notes :')
                #     note_taking.add_note(id_ = usr_id,title= title, note= notes)
                #     to_json('Done , to view. say, view notes')
                # if tag == 'delete-notes':
                #     to_json('which node to delete')
                #     print(note_taking.list_notes(id_ = usr_id).keys())
                #     title = input('enter title :')
                #
                #     to_json('deleted successfully')
                # if tag == "read-notes":
                #     notes = note_taking.list_notes(id_ = usr_id)
                #     num =0
                #     print(notes.keys())
                #     to_json(f"you have {len(notes)} notes named {converttostring(notes.keys())} . Type the name of notes you are looking for")
                #     title  = input('Title :')
                    # try :
                    #     to_json('should i read the notes for you?')
                    #     read = takeCommand().lower()
                    #     tag = prediction(read)
                    #     if tag == 'agree':
                    #         to_json(f'title :{title} \n Note : {notes[title]}')
                    # except :
                    #     to_json(f'title {title} .  could not open, please write title correctly')

            except Exception as e:
                stuff_for_frontend = to_json('sorry something went wrong')
                # print(e)

    return stuff_for_frontend


# while True:
#      x = input('user : ')
#      print(miku_speak(takeCommand(x).lower()))
