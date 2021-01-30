from django.db.models.base import Model
from django.shortcuts import render, HttpResponse
from Backend import assistant
from django.http import JsonResponse, HttpResponse
from Backend.AssistantFunctions import database, websearch
import json
from . import models
# Create your views here.


def home(request):
    x = request.user
    print(x.id)
    return render(request, 'Mainapp/base.html')


def feedbackpage(request):
    # length = models.feedback.objects.all().count()
    data_obj = models.feedback.objects.all().order_by("user")
    # print(data_obj)
    return render(request, 'Mainapp/feedback.html', {
        "feedback": data_obj})


def searchengine(request, query):
    result = websearch.bingsearch(query)
    links = result['webPages']['value']
    urlsntitles = []
    for link in links:
        snippet = link['snippet'].replace(
            '<b>', '')
        snippet = snippet.replace(
            '</b>', '')
        urlsntitles.append((link['name'], link['url'], snippet))
        # print(urlsntitles)
    # print(urlsntitles)
    # return JsonResponse(result)
    return render(request, 'Mainapp/websearch.html', {
        "web": urlsntitles})


def test(request):

    return render(request, 'Mainapp/test.html')


def music(request):

    return render(request, 'Mainapp/Music.html')


def test(request):

    return render(request, 'Mainapp/test.html')


def response(request, content):
    print(content)
    data = assistant.miku_speak(content)

    return JsonResponse(data)


def userdata(request):
    username = request.user
    userid = request.user.id
    usertodo = len(database.list_tasks(userid))
    print(usertodo)
    usernotes = len(assistant.noteslist(userid))
    print(usernotes)
    userdata = {
        "username": str(username),
        "userid": str(userid),
        "usertodo": str(usertodo),
        "usernotes": str(usernotes)
    }

    return JsonResponse(userdata)


def sendnotes(requests, title, notes):

    data = {
        'id': requests.user.id,
        'title': title,
        'notes': notes,
    }
    result = assistant.sendnotes(data)  # notes is dictionary
    if result:
        stuff = {
            "response": "Done",
        }
    else:
        stuff = {
            "response": "sorrt some thing whent wrong",
        }
    return JsonResponse(stuff)


def deletenotes(requests, title):

    data = {
        'id': requests.user.id,
        'title': title,
    }
    done = assistant.deletenotes(data)

    if done:
        stuff = {
            "response": "successfully deleted your note"
        }
    else:
        stuff = {
            "response": "successfully deleted your note"
        }
    return JsonResponse(stuff)


def shownotes(requests):
    result = assistant.noteslist(requests.user.id)
    if result != False:
        stuff = {
            "amount":  len(result),
            "titles": result
        }
    else:
        stuff = {
            "amount":  0,
            "titles": None
        }
    return JsonResponse(stuff)


def readnotes(requests, title: str):
    result = assistant.readnotes(usr_id=requests.user.id, title=title)
    if result != False:
        stuff = {
            "response": result
        }
    else:
        stuff = {
            "response": "sorry i could not find your notes"
        }
    return JsonResponse(stuff)


def getjoke(requests):
    stuff = {
        "response": assistant.getjokes()
    }
    return JsonResponse(stuff)


def getmeme(requests):
    memes = assistant.get_meme()
    # print(memes)
    meme = {
        "title": memes[0],
        "url": memes[1],
    }
    return JsonResponse(meme)


def username(requests):
    try:
        name = f'{requests.user.first_name} {requests.user.last_name}'
    except:
        try:
            name = f'{requests.user.first_name}'
        except:
            name = None

    name_json = {
        'name': name
    }

    return JsonResponse(name_json)


def feedback(requests, value: str):
    try:
        data = models.feedback.objects.create(
            user=str(requests.user), value=value)
        result = {"response": "thanks for your feedback"}
    except Exception as e:
        print(e)
        try:
            data = models.feedback.objects.create(
                user=str(requests.user.id), value=value)
            result = {"response": "thanks for your feedback!"}
        except:
            result = {
                "response": "sorry something went wrong. could not send your feedback"}

    return JsonResponse(result)
