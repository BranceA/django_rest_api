from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers

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

# curl -v http://localhost:8000/person_api/person-list/
@api_view(['GET'])
def ShowAll(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ShowById(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreatePerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(date_joined = date.today())

    return Response(serializer.data)

@api_view(['PUT'])
def UpdatePerson(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save(date_updated = date.today())

    return Response(serializer.data)