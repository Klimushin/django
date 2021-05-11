from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def product_list(request):
    products = [
        {"title": "Product #1", "url": "product-1"},
        {"title": "Product #2", "url": "product-2"},
        {"title": "Product #3", "url": "product-3"},
        {"title": "Product #4", "url": "product-4"},
        {"title": "Product #5", "url": "product-5"},
        {"title": "Product #6", "url": "product-6"},
        {"title": "Product #7", "url": "product-7"},
    ]
    context = {
        'count': products.__len__(),
        'title': 'Product list',
        'products': products,
    }
    return render(request, "product.html", context)


def product_detail(request, product_slug):
    return render(request, "product_detail.html", {"product_slug": product_slug})
