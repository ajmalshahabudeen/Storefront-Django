from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .models import Product, Collection, OrderItem, Review, Cart, CartItem
from .filters import ProductFilter
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer, CartItemSerializer
from .pagination import DefaultPagination

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description'] 
    ordering_fields = ['unit_price', 'last_update']
    
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
        
class CartViewSet(CreateModelMixin, 
                  RetrieveModelMixin,
                  DestroyModelMixin, 
                  GenericViewSet):
    queryset = Cart.objects.prefetch_related('items').all()
    serializer_class = CartSerializer
    
class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])