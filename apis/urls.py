# basic URL Configurations
from django.urls import include, path

# import routers
from rest_framework import routers

# import everything from views
from .views import *

router = routers.DefaultRouter()
router.register(r'stt', STTViewSet, basename="stt")

# specify URL Path for rest_framework

urlpatterns = [
    path("tts", TTSInference.as_view()),
    # path("stt", STTView.as_view()),
    path("", include(router.urls)),
]
