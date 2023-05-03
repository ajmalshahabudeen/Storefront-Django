from django.shortcuts import render
# from django.http import HttpResponse 
# from django.db.models import Q 
# from django.db.models.aggregates import Min,Max,Count,Avg 
# from store.models import Product, OrderItem 
from django.core.mail import send_mail, mail_admins, BadHeaderError

# Create your views here.
#Transform
#Send email
#Pull data from db

def say_hello(request):
    # result = Product.objects.aggregate(Count('id'),Min('unit_price'))
    # return render(request, 'hello.html', {'name': 'ajmal', 'result':result})
    try:
        mail_admins(
            'subject',
            'message',
            html_message='message'
        )
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'ajmal'})