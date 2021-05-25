from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from . models import Person
from . serializers import PersonSerializer

@api_view(['GET'])
def person_api_overview(request):
    person_api_urls = {
        'List': '/person-list',
        'Person View': '/person/<int:id>',
        'Create Person': '/person-create',
        'Update Person': '/person-update/<int:id>',
        'Delete': '/person-delete/<int:id>',
    }

    return Response(person_api_urls)

@api_view(['GET'])
def ShowAll(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)