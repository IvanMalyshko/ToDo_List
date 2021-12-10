from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
def singupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/singupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
        else:
            print('Hello')
            # Tell the user the passwords didnt match