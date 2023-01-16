from django.urls import path
from .views import (
    ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
)

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete')
]
