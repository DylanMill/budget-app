from django.shortcuts import render
from django.http import JsonResponse
from core.models import *
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from .serializers import CategorySerializer


# Create your views here.
def hello_budget(request):
    return JsonResponse({"message": "Hello, Budget App!"})


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.order_by("type", "name")
    serializer_class = CategorySerializer
