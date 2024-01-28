from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    return JsonResponse(data)