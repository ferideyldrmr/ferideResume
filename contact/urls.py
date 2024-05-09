from django.urls import path
from contact.views import contact_form


urlpatterns = [
    path('index.html', contact_form, name='k'),
]
