from django.shortcuts import render
from django.http import HttpResponse
from .models import Second_app
# Create your views here.
def home(request):
    sa1 = Second_app.objects.raw('SELECT * FROM second_app_second_app')
    return render(request,'index.html',{'sa':sa1})

def add(request):
    return HttpResponse("hello world add folder")
