from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.decorators import api_view

from api.FirstAidAssistant import generate_answer


@csrf_exempt
@api_view(['POST'])
def chat_with_bot(request):
    data = request.data
    message = data['message']
    answer = generate_answer(message)
    return JsonResponse({'answer': answer})
