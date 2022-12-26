from django.shortcuts import render
from app.forms import *
# Create your views here.

def naga(request):
    form=TopicForm()
    d={'form':form}
    if request.method=="POST":
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'naga.html',d)

def brock(request):
    form=WebpageForm()
    d1={'form':form}
    if request.method=="POST":
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'brock.html',d1)