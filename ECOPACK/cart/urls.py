from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('changecount/plus/<int:pk>/', views.product_count_plus, name='product_count_plus'),
    path('changecount/minus/<int:pk>/', views.product_count_minus, name='product_count_minus'),
    path('detail/', views.CartListView, name='cart_detail'),
]