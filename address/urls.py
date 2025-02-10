from django.urls import path

from address.views import AddressViewSet

urlpatterns = [
    path('', AddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='address-list'),
    path('<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'}), name='address-detail'),
]