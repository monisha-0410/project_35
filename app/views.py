from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import View,TemplateView
from app.forms import *


def fbv_string(request):
    return HttpResponse('This is the string from fbv_string')


class cbv_string(View):
    def get(self,request):
        return HttpResponse("This is the string of cbv_string ")
    
def fbvhtml(request):
    return render(request,'fbvhtml.html')



class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')
    



def insert_school_by_fbv(request):
    SFO=Schoolform()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')
    return render(request,'insert_school_by_fbv.html',d)


class insert_school_by_cbv(View):
    def get(self,request):
        ESFO=Schoolform()
        d={'ESFO':ESFO}
        return render(request,'insert_school_by_cbv.html',d)
    def post(self,request):
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_cbv is done')