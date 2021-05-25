from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django_rest_api/', include('django_rest_api.urls')),
]