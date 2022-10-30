from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.db.models import F

from .models import Food, FoodCategory
from .serializers import FoodCategorySerializer, FoodSerializer
# f = F(is_publish=True)


class FoodAPIView(generics.ListAPIView):
    queryset = Food.objects.filter(is_publish=True)
    serializer_class = FoodSerializer


#

class FoodListSerializerAPIListView(generics.ListAPIView):
    # queryset = FoodCategory.objects.order_by('id').filter(food__additional__is_publish=True, food__is_publish=True) # Тоже работает
    queryset = FoodCategory.objects.order_by('id').filter(food__additional__category_id__isnull=False) # Тоже работает
    # queryset = FoodCategory.objects.order_by('id').filter().distinct() # Пустая категория не публикуется больше
    serializer_class = FoodCategorySerializer
