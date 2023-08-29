from django.http import JsonResponse
from django.shortcuts import render
from chatbot.train import train
from chatbot.test import chat

def train_chatbot_api(request):
    # Call your training function here
    train()
    return JsonResponse({'message': 'Chatbot training completed successfully'})

def test_chatbot_api(request, query):
    # Call your testing function here
    response = chat(query)
    return JsonResponse({'response': response})


def index(request):
    return render(request, 'index.html')