from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('article', views.article, name='article'),
    path('hackerarticle', views.hackerarticle, name='hackerarticle'),
    path('earticle', views.earticle, name='earticle'),
    path('esports', views.esports, name='esoprts'),
    path('cities', views.cities, name='cities'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('sports', views.sports, name='sports'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('<str:val>/page/<int:num>', views.pages),
    path('hackernews', views.hackernews ),

]