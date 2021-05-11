from django.urls import path

from review.views import review

urlpatterns = [
    path('<product_slug>/<review_id>/', review),

]