from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def xyz(request):
    return render(request, "index.html")

def signUp(request):
    print("signup method is working")
    i = 10
    i =i+20
    i=i+30
    print(i)
    return render(request, "index.html")
