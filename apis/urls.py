from django.urls import path
from .views import *


# specify URL Path for rest_framework

urlpatterns = [
    path("tts", TTSInference.as_view()),
    path("stt", STTInference.as_view()),
]
