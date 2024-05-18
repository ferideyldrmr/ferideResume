from django.urls import path
from .views import index, contact, contact_form

urlpatterns = [
    path('', index, name='index'),
    path('contact_form/', contact_form, name='contact_form'),  # Updated URL pattern
]
