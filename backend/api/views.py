from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": 'Hi there, this is your Django API response'})