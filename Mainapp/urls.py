from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('response/<str:content>', views.response, name='response'),
    path('userdata/', views.userdata, name='userdata'),
    path('sendnotes/<str:title>/<str:notes>/',
         views.sendnotes, name='sendnotes'),
    path('deletenotes/<str:title>', views.deletenotes, name='deletenotes'),
    path('shownotes/', views.shownotes, name='shownotes'),
    path('readnotes/<str:title>', views.readnotes, name="readnotes"),
    path('getjoke/', views.getjoke, name="getjoke"),
    path('getmeme/', views.getmeme, name="getmeme"),
    path('test/', views.test, name="test"),
    path('music/', views.music, name="Music"),
    path('username/', views.username, name="username"),
    path('sendfeedback/<str:value>', views.feedback, name="sendfeedback"),
    path('feedback/', views.feedbackpage, name="feedback"),
    path('epaxsearch/<str:query>',
         views.searchengine, name="epaxsearch"),
]
