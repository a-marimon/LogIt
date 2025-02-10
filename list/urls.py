from django.urls import path

from list.views import ListViewSet, ItemsViewSet

urlpatterns = [
    path('', ListViewSet.as_view({'get': 'list', 'post': 'create'}), name='lists'),
    path(
        '<int:pk>/',
        ListViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update'
        }),
        name='details'
    ),
    path('items/', ItemsViewSet.as_view({'get': 'list', 'post': 'create'}), name='items'),
    path(
        'items/<int:pk>/',
        ItemsViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
            'delete': 'destroy'
        }),
        name='items'
    ),
]