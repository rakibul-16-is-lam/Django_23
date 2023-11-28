from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def Tanzil(request):
    return render(request,'html/cpi.html',{'rakib':5.00})

def rakib(request):
    return render(request,'html/ID.html')