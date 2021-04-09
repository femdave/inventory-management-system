from django.urls import path
from . import views

urlpatterns = [
    path('warehouse/', views.WarehouseCreateApiView.as_view(),
         name='add-warehouse'),
    path('category/', views.CategoryCreateApiView.as_view(), name='add-category'),
    path('product/', views.ProductCreateApiView.as_view(), name='add-product'),
    path('product/<int:id>/',
         views.ProductDetailApiView.as_view(), name='edit-product'),
]
