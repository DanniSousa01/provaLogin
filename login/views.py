from django.shortcuts import render
from . models import User

# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def login_list(request):
    users = User.objects.all()
    return render (request, 'users/list.html', {'users': users})

def login_delete(request):
    user = User.objects.get( pk = user_id)
    user.delete()
    return redirect('/login/login/')
