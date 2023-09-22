from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import GeeksModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = ["url", "title", "description"]
