from django.contrib.auth.models import Group, User 
from .models import *
from rest_framework import permissions, viewsets 
from .serializers import UserSerializer, GroupSerializer, TaskSerializer, ListTaskSerializer, PodcastSerializer, PodcastCategorySerializer, UserPodcastPoolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all().order_by("-date_finished")
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TaskListViewSet(viewsets.ModelViewSet):
    queryset = taskList.objects.all()
    serializer_class = ListTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return taskList.objects.filter(user=self.request.user)

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [permissions.IsAuthenticated]

class PodcastCategoryViewSet(viewsets.ModelViewSet):
    queryset = podcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class UserPoolPodcastViewSet(viewsets.ModelViewSet):
    queryset = userPodcastPool.objects.all()
    serializer_class = UserPodcastPoolSerializer
    permission_classes = [permissions.IsAuthenticated]