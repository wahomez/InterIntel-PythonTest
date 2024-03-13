from django.urls import path
from .views import *

urlpatterns = [
    path('bulk-insert/', bulk_insert_products, name='bulk-insert'),
]

