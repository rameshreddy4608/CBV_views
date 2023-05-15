from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.

#Function Base View
def FBV_string(request):
    return HttpResponse('This is FBV response')

#class Base View

class CBV_string(View):
    def get(self,request):
        return HttpResponse('This is CBV response')
    

#Function Base HTML view


def FBV_HTML(request):
    return render(request,'FBV_HTML.html')


#Class Base HTML view

class CBV_HTML(View):
    def get(self,request):
        return render(request,'CBV_HTML.html')
    

#Handling Form by using FBV

def FBV_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()

        return HttpResponse('data inserted')
    return render(request,'FBV_form.html',d)



#Handling form by using CBV



class CBV_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_form.html',d)
    def post(self,request):
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
            
        return HttpResponse("data inserted sucessfully")






