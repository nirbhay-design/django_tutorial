from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html",{'name':"nirbhay"})

def add(request):
    # print(request.POST)
    num1 = request.POST['num1'][0]
    num2 = request.POST['num2'][0]
    num3 = int(num1) + int(num2)
    return render(request,"home.html",{"name":num3})