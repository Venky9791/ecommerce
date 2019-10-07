from django.views.generic import ListView
from django.shortcuts import render

from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'Products/list.html'

    def get_context_data(self, *args , **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        print(context)
        return context


def Product_List_View(request):
    queryset = Product.objects.all()
    context = {'object_list':queryset}
    return render(request,'Products/list.html',context)


def __str__(self):
    return self.title,self.description,self.price
