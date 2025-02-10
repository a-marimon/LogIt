from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from list.models import List, ListItem
from list.serializers import ListSerializer, ItemSerializer


class ListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = ListSerializer
    queryset = List.objects.all()


class ItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = ItemSerializer
    queryset = ListItem.objects.all()