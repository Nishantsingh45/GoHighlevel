
from django.urls import path
from . import views

urlpatterns = [
    path('update_custom_field/', views.update_custom_field, name='update_custom_field'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
    # Add other URLs if needed
]