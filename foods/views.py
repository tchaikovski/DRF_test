from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Food, FoodCategory, FoodListSerializer, FoodSerializer


class FoodAPIView(generics.ListAPIView):
    queryset = Food.objects.filter(is_publish=True)
    serializer_class = FoodSerializer
#

class FoodAPIListView(generics.ListAPIView):
    queryset = FoodCategory.objects.order_by('id').filter(food__additional__is_publish=True) # Тоже работает
    # queryset = queryset.filter(food__is_publish=True)
    # queryset = FoodCategory.objects.order_by('id').filter(food__additional__category_id__isnull=False) # Пустая категория не публикуется больше
    serializer_class = FoodListSerializer
