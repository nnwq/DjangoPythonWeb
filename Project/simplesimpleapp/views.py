from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView
)

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product


# Create your views here.
class ProductList(ListView):
    model = Product
    ordering = 'name'   # filter filed
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 5

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
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'

