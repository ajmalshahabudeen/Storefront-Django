from . import views
from django.urls import path
from rest_framework_nested import routers
from pprint import pprint

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='products')
products_router.register('reviews', views.ReviewViewSet, basename='product-review')

urlpatterns = router.urls + products_router.urls

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
