from django.urls import path
from . import views
from django.urls import reverse_lazy


urlpatterns = [
    path('detail/', views.OrderList, name='orders_detail'),
    path('manager_detail/', views.AllOrderList, name='manager_order_details'),
    path('add/', views.OrderAdd, name='order_add'),
    path('<int:pk>/edit', views.OrderUpdateView.as_view(), name='order_edit'),
    path('status_edit/<int:pk>', views.OrderStatusEdit, name='order_status_edit'),
]