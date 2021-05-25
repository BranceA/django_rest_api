from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
def person_api_overview(request):
    person_api_urls = {
        'List': '/person-list/',
        'Person View': '/person/<int:id>',
        'Create Person': '/person-create/',
        'Update Person': '/person-update/<int:id>',
        'Delete': '/person-delete/<int:id>',
    }

    return Response(person_api_urls)