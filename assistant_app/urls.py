from django.urls import path
from .views import get_response
from .views import home

urlpatterns = [
    path('get_response/', get_response, name='get_response'),
    path('', home, name='home'),
]
