from django.urls import path
from . import views
from .views import JobViewSet

# URLConf
urlpatterns = [
    path('', JobViewSet.as_view({'get': 'list', 'post': 'create'}), name='job-list'),
    path(
        '<int:pk>/',
        JobViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='job-detail'
    ),
]