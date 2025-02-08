from rest_framework import serializers

from list.models import List, ListItem


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = '__all__'