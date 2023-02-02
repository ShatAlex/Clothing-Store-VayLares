from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from clothes.models import *
from clothes.utils import DataMixin
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    if 'select_size' in request.POST:
        size_id = request.POST['select_size']
        product = get_object_or_404(Sizes_of_Clothes, id_clothes=product_id, id_size=size_id)
    else:
        product = get_object_or_404(Sizes_of_Clothes, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    else:
        cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart:cart_detail')


class Basket(DataMixin, ListView):
    model = Clothes
    template_name = 'clothes/basket.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        c_def = self.get_user_context(title='Корзина', cart=cart)
        return dict(list(context.items()) + list(c_def.items()))