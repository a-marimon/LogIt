from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from equipment.models import Equipment
from equipment.serializers import EquipmentSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
