from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h1>장고공부를 재미있게 합시다!</h1>")

def getname(request):
    name=request.GET['studentname']
    print(f'클라이언트에서 보내온 이름 : {name}')
    return HttpResponse("<h1>당신의 이름은"+name+"이군요</h1>")