from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("This is January!")

def february(request):
    return HttpResponse("This is february...")

def march(request):
    return HttpResponse("Learn Django for at least 20 minutes every day.")

