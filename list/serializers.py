from django.utils.functional import empty
from rest_framework import serializers

from list.models import List, ListItem


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=False)

    class Meta:
        model = List
        fields = '__all__'
