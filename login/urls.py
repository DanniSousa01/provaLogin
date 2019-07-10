from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_list),
    path('users/delete/<int:user_id>/', views.login_delete)
    ]