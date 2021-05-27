from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_api_overview, name='personApiOverview'),
    path('person-list/', views.ShowAll, name='person-list'),
    path('person/<int:pk>', views.ShowById, name='single-person'),
    path('create-person/', views.CreatePerson, name='create-person'),
    path('update-person/<int:pk>', views.UpdatePerson, name='update-person'),
    path('delete-person/<int:pk>', views.DeletePerson, name='delete-person'),
    path('job-list/', views.ShowAll, name='job-list'),
    path('job/<int:pk>', views.ShowById, name='single-job'),
    path('create-job/', views.CreateJob, name='create-job'),
]