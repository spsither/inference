from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apis.serializers import UserSerializer, GroupSerializer

# import local data
from .serializers import STTSerializer, TTSSerializer, UploadSerializer
from .models import STTModel, TTSModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.http import Http404

# from .serializers import UploadSerializer

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

        return Response({"text": text}, status=status.HTTP_200_OK)

class STTView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return STTModel.objects.get(pk=pk)
        except STTModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = STTSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = STTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class STTViewSet(viewsets.ModelViewSet):
    queryset = STTModel.objects.all()
    serializer_class = STTSerializer

    def pre_save(self, obj):
        obj.audio = self.request.FILES.get('audio')
