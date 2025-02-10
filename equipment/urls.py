from django.urls import path

from address import views
from equipment.views import EquipmentViewSet

urlpatterns = [
    path('', EquipmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='equipment-list'),
    path(
        '<int:pk>/',
        EquipmentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch:': 'partial_update',
            'delete': 'destroy'
        }),
        name='equipment-detail'
    ),
]