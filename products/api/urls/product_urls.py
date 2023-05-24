from django.urls import path
from products.api.views import product_views as views

urlpatterns = [
    path('', views.get_products, name="products"),
    path('<int:product_id>/', views.get_product_details, name="product_details"),
    path('categories/', views.get_categories, name="categories"),
    path('stocks/<int:product_id>/', views.get_stock, name="stocks"),
]
