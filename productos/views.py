from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
   
class ProductDetailView(DetailView):
    model = Product 
    template_name = 'product.html'
    
class ProductSearchListView(ListView):
    template_name= 'search.html'
    
    def get_queryset(self):
        return Product.objects.filter(tittle__icontains=self.query())
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_content_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context 