from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime


# Create your views here.
class ProductList(ListView):
    model = Product
    ordering = 'name'   # filter filed
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'Sale is on wednesday'
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
