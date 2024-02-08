from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('hello/', views.say_hello, name='say_hello')
]