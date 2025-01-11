from django.urls import path
from .views import hello,user

app_name='first'
urlpatterns = [
    path('',hello,name='hello'),
    path('users',user),
]
