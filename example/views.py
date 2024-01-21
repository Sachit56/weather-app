# example/views.py
from datetime import datetime
from django.shortcuts import redirect,render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi')