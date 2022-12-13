from django.urls import path
from . import views
from .views import image_request

urlpatterns = [
    path('', views.ProductListView, name='product_list'),
    path('new/',  image_request, name='product_create'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('quan/', views.quan_ren, name='quan_ren'),]