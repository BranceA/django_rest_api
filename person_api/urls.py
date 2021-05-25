from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_api_overview, name='personApiOverview'),
    path('person-list/', views.ShowAll, name='person-list')
]