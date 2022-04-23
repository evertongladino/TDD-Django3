from django import http
from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'animais/index.html')