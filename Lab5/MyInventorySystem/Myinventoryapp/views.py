from django.shortcuts import render
from .models import Supplier
from .models import WaterBottle

# Create your views here.
def hello_world(request):
    return render(request, 'Myinventoryapp/hello_world.html')

def view_supplier(request):
    # Variable Name to be Changed Later if create separate template.html file
    varName = Supplier.objects.all()
    return render(request, 'Myinventoryapp/base_template.html', {'Supplier': varName})

def view_bottles(request):
    # Variable Name to be Changed Later
    varName = WaterBottle.objects.all()
    return render(request, 'Myinventoryapp/base_template.html', {'WaterBottle': varName})

def add_bottle(request):
    return render(request, 'Myinventoryapp/base_template.html')