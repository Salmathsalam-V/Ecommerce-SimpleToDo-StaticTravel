from django.shortcuts import render
from shop . models import Product
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(Name__contains=query) | Q(Description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})