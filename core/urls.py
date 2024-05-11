from django.urls import path
from .views import index, contact, contact_form

urlpatterns = [
    path('', index, name='index'),
    path('index.html', contact_form, name='contact_form'),
]
