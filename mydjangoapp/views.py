from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcomefunc(request):
    return HttpResponse("Welcome")

def hello(reqhello):
    return render(reqhello,'index.html')
