from Mainapp import models
from django.db.models.base import Model
from django.shortcuts import render, HttpResponse
from Backend import assistant
from django.http import JsonResponse, HttpResponse, request
from Backend.AssistantFunctions import websearch
import json
from .models import Todo, UserNotes as Notes, Todo

# Create your views here.


def home(request):
    return render(request, 'Mainapp/base.html')


def response(request, content):
    print(content)
    data = assistant.assistant_response(content)

    return JsonResponse(data)


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


def userdata(request):
    username = request.user
    userid = request.user.id
    usertodo = len(Todo.objects.filter(user=request.user))
    usernotes = len(Notes.objects.filter(user=request.user))

    userdata = {
        "username": str(username),
        "userid": str(userid),
        "usertodo": str(usertodo),
        "usernotes": str(usernotes)
    }

    return JsonResponse(userdata)


def sendnotes(requests, title, notes):
    notes = Notes.objects.create(user=requests.user, title=title, value=notes)
    notes.save()

    print(notes)
    stuff = {
        "response": "Done Say show notes to view",
    }
    return JsonResponse(stuff)


def deletenotes(requests, title):
    notes = Notes.objects.filter(user=requests.user).get(title=title)
    notes.delete()
    stuff = {
        "response": "successfully deleted your note"
    }
    return JsonResponse(stuff)


def shownotes(requests):
    data = Notes.objects.filter(user=requests.user).order_by("-date")
    print(data)
    stuff_for_frontend = {}
    for note in data:
        stuff_for_frontend[note.title] = note.value

    # print([i.title for i in data])
    stuff = {
        "amount":  len(stuff_for_frontend),
        "titles": stuff_for_frontend
    }
    return JsonResponse(stuff)


def readnotes(requests, title: str):

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


def feedbackpage(request):
    # length = models.feedback.objects.all().count()
    data_obj = models.feedback.objects.all().order_by("user")
    # print(data_obj)
    return render(request, 'Mainapp/feedback.html', {
        "feedback": data_obj})
