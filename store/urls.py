from . import views
from django.urls import path

urlpatterns = [
    path ('products/', views.product_list),
    path ('products/<int:id>/', views.product_detail),
    path ('collection/<int:pk>/', views.collection_detail, name='collection-detail'),
]
