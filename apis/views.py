from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apis.serializers import UserSerializer, GroupSerializer
from .models import STTModel, TTSModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import os
import datetime


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TTSInference(APIView):
    def post(self, request):
        text = request.data.get("text")

        if not text:
            return Response(
                {"error": "text required to run TTS."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(text) > 300:
            return Response(
                {"error": "text must be less than 300 characters."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task = TTSModel.objects.create(text=text, user=request.user)
        task.save()
        return Response({"text": text}, status=status.HTTP_200_OK)


class STTInference(APIView):
    def post(self, request):
        audio = self.request.FILES.get("audio")
        if not audio:
            return Response(
                {"error": "audio required to run STT."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ext = os.path.splitext(audio.name)[1]
        valid_extensions = [".wav", ".mp3"]
        if not ext.lower() in valid_extensions:
            # print(ext.lower())
            return Response(
                {"error": "audio must be if wav or mp3 type."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        basename = request.user.username
        suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        audio.name = "_".join([basename, suffix]) + ext
        task = STTModel.objects.create(audio=audio, user=request.user)
        task.save()

        # run inference
        task.text = "bla bla"
        task.save()
        return Response({"text": task.text}, status=status.HTTP_200_OK)
