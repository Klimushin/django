from django.urls import path
from product.views import homepage, contacts, product_list, product_detail

urlpatterns = [
    path('', homepage, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('product/', product_list, name="list"),
    path('product/<product_slug>', product_detail, name="detail"),

]