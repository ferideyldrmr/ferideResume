from django.urls import path
from contact.views import contact_form,index

urlpatterns = [
    path('', index, name='index'),
    path('index.html', contact_form, name='contact_form'),
]
