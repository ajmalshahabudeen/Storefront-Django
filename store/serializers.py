from rest_framework import serializers
from store.models import Product, Collection
from decimal import Decimal

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection'] 

 
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # price_with_tax = serializers.SerializerMethodField(
    #     method_name= 'calculate_tax'
    # )
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name='collection-detail'
    # )
    
    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)