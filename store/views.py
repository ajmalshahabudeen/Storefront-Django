from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Collection, OrderItem, Review
from .filters import ProductFilter
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    
    def get_serializer_context(self):
        return {'request':self.request} 
    
    def destroy(self, request, *args, **kwargs):     
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0: # related_name='orderitems' in models.py under OrderItem class product object 
            return Response(
                {"error":"product cannot be deleted because it is associated with order item"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
            products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Collection.objects.filter(id=kwargs['pk']).count() > 0: # related_name='orderitems' in models.py under OrderItem class product object 
            return Response(
                {"error":"This collection cannot be deleted because it contains one or more items"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['products_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['products_pk']}
        # we pass this dictionary to serializer