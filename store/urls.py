from . import views
from django.urls import path
from rest_framework_nested import routers
# from pprint import pprint

# for normal routers
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet) 
router.register('customers', views.CustomerViewSet) 
router.register('orders', views.OrderViewSet, basename='orders') 
# pprint(router.urls)

# for nested routers
products_router = routers.NestedDefaultRouter(router, 'products', lookup='products')
products_router.register('reviews', views.ReviewViewSet, basename='product-review')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-item')

urlpatterns = router.urls + products_router.urls + carts_router.urls

# we can also explicitly define
# [
#     path(r'', include(router.urls)),
#     path(r'', include(products_router.urls))
# ]

# [
#     path ('products/', views.ProductList.as_view()),
#     path ('products/<int:pk>/', views.ProductDetail.as_view()),
#     path ('collections/', views.CollectionList.as_view()),
#     path ('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
# ]
