from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('',views.register,name="register"),
    path('profile/',views.profilepage,name="profile"),
]