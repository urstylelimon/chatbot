# bot/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .chat import get_chatbot_response

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        chatbot_response = get_chatbot_response(user_input)
        return JsonResponse({'response': chatbot_response})
    return render(request, 'chat.html')
