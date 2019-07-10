from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def login_list(request):
    users = User.objects.all()
    return render (request, 'users/list.html', {'users': users})

@permission_required("user_delete")
def login_delete (request, user_id):
    user = User.objects.get(pk = user_id)
    user.delete()
    return redirect('/login/login/')

