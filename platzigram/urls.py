""" El modulo de url de platzigram === Son las encargadas de encontrar el recurso"""
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/',local_views.hi),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/',posts_views.list_posts),
]

