from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from cart.models import Product_in_cart

from . import forms
from . import models

def quan_ren(request):
    products = models.Product.objects.all()
    try:
        number_of_positions = len((Product_in_cart.objects.get(user_id=request.user.pk)).products['products'])
    except:
        number_of_positions = 0
    return render(request,'none.html', {'cart_num':number_of_positions})


def ProductListView(request):
    products = models.Product.objects.all()
    try:
        number_of_positions = len((Product_in_cart.objects.get(user_id=request.user.pk)).products['products'])
    except:
        number_of_positions = 0
    categories = []
    for index in range(len(products)):
        if products[index].category in categories:
            pass
        else:
            categories.append(products[index].category)
    return render(request, 'product_list.html',
                  {'object_list': products,  'cart_num': number_of_positions, 'categories': categories})


def image_request(request):
    if request.method == 'POST':
        form = forms.UserImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'product_create.html', {'form': form, 'img_obj': img_object})
    else:
        form = forms.UserImage()

    return render(request, 'product_create.html', {'form': form})



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    login_url = 'login'



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Product
    fields = ['name', 'price', 'size', 'layer_field', 'category', 'description', 'photo']
    template_name = 'product_edit.html'
    login_url = 'login'



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

