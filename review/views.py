from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def review(request, product_slug, review_id):
    return HttpResponse(f'This is a review {review_id} for {product_slug}')
