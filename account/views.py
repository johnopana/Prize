from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'account/dashboard.html')
def product(request):
    return render(request,'account/product.html')
def customer(request):
    return render(request,'account/customer.html')       

# Create your views here.
