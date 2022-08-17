from django.urls import path, include

from home.views import *

urlpatterns = [
    path('', index, name='home'),
    path('servis/<int:ser>/', services),
    path('about/', about, name='about'),
    path('reviews/', reviews, name='reviews'),
    path('contact/', contact, name='contact'),
    path('services/<int:services_id>/',show_services, name='services'),
]
