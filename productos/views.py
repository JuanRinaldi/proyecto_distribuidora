from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_content_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        
        return context
    
class ProductDetailView(DetailView):
    model = Product 
    template_name = 'product.html'