from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('lastday', last_day),
    path('lastmonth', last_month),
    path('rating', service_rating),
    path('published', service_published_rating),
]
