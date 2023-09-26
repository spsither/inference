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
    user = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model = STTModel
        fields = ["text", "audio", "user"]
    # def validate_audio(self, value):
    #     import os
    #     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    #     valid_extensions = ['.wav', '.mp3']
    #     if not ext.lower() in valid_extensions:
    #         raise serializers.ValidationError('audio_file must be wav or mp3.')
    #     return value
    # def validate(self, data):
    #     """
    #     Check that the audio is wav or mp3 file.
    #     """
    #     import os
    #     ext = os.path.splitext(data.name)[1]  # [0] returns path+filename
    #     valid_extensions = ['.wav', '.mp3']
    #     if not ext.lower() in valid_extensions:
    #         raise serializers.ValidationError('audio_file must be wav or mp3.')
    #     return data

class TTSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TTSModel
        fields = ["text", "audio", "user"]

class UploadSerializer(Serializer):
    audio_file = FileField()
    class Meta:
        fields = ['audio_file']
    def validate(self, data):
        """
        Check that the audio is wav or mp3 file.
        """
        import os
        ext = os.path.splitext(data.name)[1]  # [0] returns path+filename
        valid_extensions = ['.wav', '.mp3']
        if not ext.lower() in valid_extensions:
            raise serializers.ValidationError('audio_file must be wav or mp3.')
        return data