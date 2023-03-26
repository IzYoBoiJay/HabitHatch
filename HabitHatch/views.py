from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
def mainpage(request):
    return render(request, 'base.html')


def choreselecting (request):
    form = choreForm()
    if request.method == 'POST':
        form = choreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'chores.html', context)

def login(request):
    return render(request, 'login.html')

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