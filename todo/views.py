from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def singupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/singupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/singupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'todo/singupuser.html', {'form':UserCreationForm(), 'error':'Password did not match'})


def currenttodos(request):
    return render(request, 'todo/currenttodos.html')