from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#takes a request and returns a response
#request handeler

def say_hello(request):
   
    return render(request,'hello.html', {'age':'20'})    