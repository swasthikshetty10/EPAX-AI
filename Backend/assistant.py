from nltk.stem import WordNetLemmatizer
import nltk
from os.path import join
from urllib.request import urlopen
import json
import numpy as np
from pyjokes import jokes_de
from tensorflow import keras
import pickle
#from googletrans import Translator
import random
from tensorflow.keras.models import load_model
#### importing functions ####
from Backend.AssistantFunctions import codehelp, questions, jokes, rps, whatis, news, pymemes, translate__
#translator = Translator()
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


model = load_model('Trained_Models/bot.h5')
intents = json.loads(open('Trained_Models/intents.json').read())
words = pickle.load(open('Trained_Models/words.pkl', 'rb'))
classes = pickle.load(open('Trained_Models/classes.pkl', 'rb'))
#### Predictions  ################


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
        if 'what is' in pattern or 'who is' in pattern or 'what\'s' in pattern:
            mlquestions.append(pattern)

howdo = [
    "how do",
    "how to",
]

# main


def getjokes():
    return jokes.pyjoke()


def get_meme():
    memes = pymemes.get_meme('ProgrammerHumor')
    return random.choice(memes)


##### response #####

def assistant_response(query):
    stuff_for_frontend = None
    if query != 'none':
        # search google and wolfarm alpha ,
        if ('what\'s' in query or 'what is' in query or 'where is' in query or 'which is' in query or 'who is' in query) and query not in mlquestions:
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

            try:

                stuff_for_frontend = prediction(query)
                tag = stuff_for_frontend.get('tag')
                # open stack overflow
                if tag == 'stackoverflow':

                    stuff_for_frontend = to_json(
                        response='oh but i cant fix your error right now')

            except Exception as e:
                stuff_for_frontend = to_json('sorry something went wrong')

    return stuff_for_frontend
