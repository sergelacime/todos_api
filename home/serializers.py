from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','password','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# home models
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

class ListTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = taskList
        fields = '__all__'

class PodcastCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = podcastCategory
        fields = '__all__'

class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = podcast
        fields = '__all__'

class UserPodcastPoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userPodcastPool
        fields = '__all__'