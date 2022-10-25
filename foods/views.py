from rest_framework import generics
from django.shortcuts import render

from .models import Food, FoodListSerializer, FoodSerializer


class FoodAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
class FoodAPIListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer