from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
#Transform
#Send email
#Pull data from db

def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(20,30))
    return render(request, 'hello.html', {'name': 'ajmal', 'products': list(queryset)})

