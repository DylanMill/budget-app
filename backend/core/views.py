from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def hello_budget(request):
    return JsonResponse({"message": "Hello, Budget App!"})
