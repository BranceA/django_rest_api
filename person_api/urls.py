from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_api_overview, name='person_api_overview'),
]