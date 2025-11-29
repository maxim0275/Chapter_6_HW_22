from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home_view, name='home_view'),
    path('contacts/', views.contacts_view, name='contacts_view')
]
