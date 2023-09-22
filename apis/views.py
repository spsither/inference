from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apis.serializers import UserSerializer, GroupSerializer
# import local data
from .serializers import GeeksSerializer
from .models import GeeksModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = GeeksModel.objects.all()
 
    # specify serializer to be used
    serializer_class = GeeksSerializer

class TTSInference(APIView):
    def get(self, request):
        text = request.data.get('text')
        
        if not text:
            return Response({'error': 'text required to run TTS.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'text': text}, status=status.HTTP_200_OK)