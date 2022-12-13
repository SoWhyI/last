from django.shortcuts import render
from . import models
from products.models import Product
from products.views import ProductListView
from users.models import CustomUser
import json


def CartListView(request):
    user_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)
    sum_of_prices = 0
    products_list = []

    try:
        for pr in user_cart.products['products']:
            product = Product.objects.get(id = pr['id'])
            sum_of_prices += int(pr['quan']) * float(product.price)
            product.price = product.price * int(pr['quan'])
            product.quantity_in_cart = int(pr['quan'])
            products_list.append(product)
        number_of_positions = len(user_cart.products['products'])
    except:
        number_of_positions = 0

    return render(request, 'cart_detail.html', {'object_list': products_list, 'sum': sum_of_prices, 'cart_num': number_of_positions, 'user': CustomUser.objects.get(id=request.user.id)})


def cart_add(request, product_id):

    try:
        object = models.Product_in_cart.objects.get(user_id=request.user.pk)
        if object.user_id == request.user:
            for index in range(len(object.products['products'])):
                if object.products['products'][index]['id'] == product_id:
                    object.products['products'][index]['quan'] += 1
                    object.save()
                    return ProductListView(request)

            object.products['products'].append(json.loads('{"id":%s, "quan": 1}' % (product_id)))
            object.save()
            return ProductListView(request)
    except:
        data = json.loads('{"products": [{"id":%s, "quan": 1}]}' % (product_id))
        new_cart = models.Product_in_cart.objects.create(user_id=request.user, products=data)
    return ProductListView(request)



def product_count_plus(request, pk):
    user_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)
    for index in range(len(user_cart.products['products'])):
        if user_cart.products['products'][index]['id'] == pk:
            user_cart.products['products'][index]['quan'] += 1
            user_cart.save()
    return CartListView(request)


def product_count_minus(request, pk):
    user_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)
    for index in range(len(user_cart.products['products'])):
        if user_cart.products['products'][index]['id'] == pk:
            user_cart.products['products'][index]['quan'] -= 1
            if user_cart.products['products'][index]['quan'] <= 0:
                user_cart.products['products'].pop(index)
        user_cart.save()
    return CartListView(request)


def product_delete(request, product_id):
    user_cart = models.Product_in_cart.objects.get(user_id=request.user.pk)
    for index in range(len(user_cart.products['products'])):
        if user_cart.products['products'][index]['id'] == product_id:
            user_cart.products['products'].pop(index)
            user_cart.save()
            return CartListView(request)
    return CartListView(request)



