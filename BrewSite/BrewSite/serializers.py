from django.forms import widgets
from rest_framework import serializers
from BrewSite.models import Brew


class BrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brew
        fields = ('id', 'name', 'color')
