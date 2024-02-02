from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from store.models import Product

class Index(ListView):
    model = Product
    context_object_name = "product_list"
    template_name = 'store/index.html'

    def get_queryset(self) -> QuerySet[Product]:
        return super().get_queryset()[:6]
    
class ProductDetail(DetailView):
    model = Product
    context_object_name = "product"
    template_name = 'store/product_detail.html'
