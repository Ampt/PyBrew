from rest_framework import generics
from BrewAPI.models import Brew
from BrewAPI.serializers import BrewSerializer


class BrewList(generics.ListCreateAPIView):

    queryset = Brew.objects.all()
    serializer_class = BrewSerializer


class BrewDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Brew.objects.all()
    serializer_class = BrewSerializer
