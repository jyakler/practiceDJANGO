from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h1>장고공부를 재미있게 합시다!</h1>")