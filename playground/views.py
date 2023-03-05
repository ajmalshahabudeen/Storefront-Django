from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product

# Create your views here.
#Transform
#Send email
#Pull data from db

def say_hello(request):
    queryset = Product.objects.values('id','title','collection__title')
    return render(request, 'hello.html', {'name': 'ajmal', 'products': list(queryset)})

