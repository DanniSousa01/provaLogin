from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_list),
    path('users/login_delete/<int:id>/', views.login_delete)
    ]