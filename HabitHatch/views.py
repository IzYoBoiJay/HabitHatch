from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
def mainpage(request):
    return render(request, 'base.html')


def choreselecting (request):
    return render(request, 'chorechoosing.html')

def register(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully') 
            return HttpResponseRedirect('/choreselecting') 
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)  