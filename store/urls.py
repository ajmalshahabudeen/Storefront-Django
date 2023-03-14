from . import views
from django.urls import path

urlpatterns = [
    path ('products/', views.ProductList.as_view()),
    path ('products/<int:pk>/', views.ProductDetail.as_view()),
    path ('collections/', views.CollectionList.as_view()),
    path ('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
]
 