from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import STTModel, TTSModel
from rest_framework.serializers import Serializer, FileField

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


# Create a model serializer
class STTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = STTModel
        fields = ["text", "audio", "user"]

class TTSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TTSModel
        fields = ["text", "audio", "user"]