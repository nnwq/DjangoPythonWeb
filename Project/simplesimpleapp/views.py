from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime
from .filters import ProductFilter


# Create your views here.
class ProductList(ListView):
    model = Product
    ordering = 'name'   # filter filed
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
