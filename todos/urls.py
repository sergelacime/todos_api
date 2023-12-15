from django.urls import include, re_path
from rest_framework import routers 
from home import views 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'UserTasksList', views.TaskListViewSet)
router.register(r'Podcast', views.PodcastViewSet)
router.register(r'Podcast_category', views.PodcastCategoryViewSet)
router.register(r'Podcast_user_pool', views.UserPoolPodcastViewSet)

urlpatterns = [
    re_path('',include(router.urls)),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls