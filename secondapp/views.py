from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def exam1(request):
    template=loader.get_template('exam1.html')
    return HttpResponse(template.render(None,request))