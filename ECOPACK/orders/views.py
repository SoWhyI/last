from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView
from . import models
from products.models import Product
from cart.models import Product_in_cart
import json
from django.views.generic.edit import UpdateView, DeleteView
import datetime
import random
from . import forms
from .forms import OrderManage
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def AllOrderList(request):
        user_orders = models.Order.objects.all()
        sums_of_prices = []
        for index in range(len(user_orders)):
            user_order = user_orders[index]
            sum_of_prices = 0
            products_list = []
            for pr in user_order.product_list['products']:
                product = Product.objects.get(id=pr['id'])
                sum_of_prices += int(pr['quan']) * float(product.price)
                product.price = product.price * int(pr['quan'])
                product.quantity_in_cart = int(pr['quan'])
                products_list.append(product)
            user_orders[index].product_list = products_list
            sums_of_prices.append(sum_of_prices)
        ready_orders = []
        delivering_orders = []
        preparing_orders = []
        for index in range(len(user_orders)):
            if user_orders[index].status == 'Выполнен':
                ready_orders.append(user_orders[index])
            elif user_orders[index].status == 'Доставляется':
                delivering_orders.append(user_orders[index])
            elif user_orders[index].status == 'Готовится':
                preparing_orders.append(user_orders[index])
        return render(request, 'manager_order_details.html', {'object_list': reversed(user_orders), 'ready': reversed(ready_orders),  'preparing': reversed(preparing_orders), 'delivery': reversed(delivering_orders), 'sum': sums_of_prices})
# Create your views here.   1
def OrderList(request):
    user_orders = models.Order.objects.filter(user_id=request.user.pk)
    sums_of_prices = []
    for index in range(len(user_orders)):
        order = user_orders[index]
        sum_of_prices = 0
        products_list = []
        for pr in order.product_list['products']:
            product = Product.objects.get(id=pr['id'])
            sum_of_prices += int(pr['quan']) * float(product.price)
            product.price = product.price * int(pr['quan'])
            product.quantity_in_cart = int(pr['quan'])
            products_list.append(product)
        user_orders[index].product_list = products_list
        sums_of_prices.append(sum_of_prices)
    return render(request, 'orders_detail.html', {'object_list':  reversed(user_orders), 'sum': sums_of_prices})


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Order
    form_class = OrderManage
    template_name = 'order_manager.html'
    login_url = 'login'


def OrderAdd(request):
    user_cart = Product_in_cart.objects.get(user_id=request.user.pk)
    if len(user_cart.products['products']) != 0 :
        new_order =  models.Order.objects.create(user_id=request.user, product_list=user_cart.products, order_date = datetime.datetime.now(), delivery_time=datetime.datetime.now() + datetime.timedelta(hours=random.randint(1, 5)))
        user_cart.products = json.loads('{"products": []}')
        user_cart.save()
    else:
        pass
    return OrderList(request)

def OrderStatusEdit(request, pk):
    order = models.Order.objects.get(id=pk)
    order.status = 'Выполнен'
    order.save()
    return OrderList(request)