# basic URL Configurations
from django.urls import include, path

# import routers
from rest_framework import routers

# import everything from views
from .views import *


# specify URL Path for rest_framework

urlpatterns = [
    path("tts", TTSInference.as_view()),
    path("stt", STTInference.as_view()),
]
