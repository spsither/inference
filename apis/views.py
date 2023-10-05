from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apis.serializers import UserSerializer, GroupSerializer
from .models import STTModel, TTSModel, State
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import datetime
from django.http import FileResponse
import magic
from django.conf import settings
import pathlib


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

        # run inference
        task.audio = STTModel.objects.get(id=14).audio
        task.save()
        task.state = State.DONE
        return FileResponse(task.audio.open())


class STTInference(APIView):
    def post(self, request):
        # validation
        audio = self.request.FILES.get("audio")
        if not audio:
            return Response(
                {"error": "audio required to run STT."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ext = pathlib.Path(audio.name).suffix
        if not ext.lower() in settings.VALID_EXTENSIONS:
            return Response(
                {
                    "error": f"audio must have {' or '.join(settings.VALID_EXTENSIONS)} extension."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        frag = request.FILES["audio"].read(1024)
        content_type = magic.from_buffer(frag, mime=True)
        print(content_type)
        if not content_type in settings.VALID_MIME_TYPES:
            return Response(
                {
                    "error": f"audio must be of {' or '.join(settings.VALID_EXTENSIONS)} type."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # save audio
        basename = request.user.username
        suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        audio.name = "_".join([basename, suffix]) + ext
        task = STTModel.objects.create(audio=audio, user=request.user)
        task.save()

        # run inference

        # update task
        task.text = "bla bla"
        task.state = State.DONE
        task.save()
        return Response({"text": task.text}, status=status.HTTP_200_OK)
