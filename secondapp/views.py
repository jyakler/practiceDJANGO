from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def exam1(request):
    template=loader.get_template('exam1.html')
    return HttpResponse(template.render(None,request))

def exam2(request) :
    name = request.GET.get('name', "유니코")
    context = {'result' : name}
    return render(request, 'exam2.html', context)

def exam3(request) :
    context = {'number' : 5, "food" : "샌드위치"}
    return render(request, 'exam3.html', context)

def exam4(request) :
    context = {'numbers':[1,2,3,4,5,6]}
    return render(request, 'exam4.html', context)
    #return render(request, 'exam4_1.html', context)

def exam5(request) :
    name = request.GET.get('name', "게스트")
    address = request.GET.get('address', "작성안함")
    context = { 'name':name, 'address':address }
    return render(request, 'exam5.html', context)

def exam6(request) :
    if request.method == 'POST':
        num = int(request.POST['number'])
        context = { 'num' : num*num }
    else :
        context = None
    return render(request, 'exam6.html', context)