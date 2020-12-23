from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from events.models import EventCategory, Event 
from events.views import EventListView
from .forms import CreateUserForm, LoginForm






@login_required(login_url='login')
def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    events = Event.objects.all()
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events
    }
    return render(request, 'dashboard.html', context)



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username = form.cleaned_data.get('username')
                groupe=Group.objects.get(name='part')
                user.groups.add(groupe)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def homepart_page(request):
    model_event = Event.objects.all().values()
    context = {
        'events': model_event,
        
    }
    
    return render(request, 'homepart.html',context)

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user.is_superuser:
                return redirect('http://127.0.0.1:8000/admin/')
            elif user.groups.filter(name='part').exists() :
                login(request, user)
                return redirect('homepart')
            elif user.groups.filter(name='org').exists() :
                login(request, user)
                return redirect('dashboard')
            
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)

def logut_page(request):
    logout(request)
    return redirect('login')