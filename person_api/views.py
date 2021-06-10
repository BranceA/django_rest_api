from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers, status

from . models import Job, Person
from . serializers import JobSerializer, PersonSerializer

@api_view(['GET'])
def person_api_overview(request):
    person_api_urls = {
        'List': '/person-list',
        'Person View': '/person/<int:id>',
        'Create Person': '/person-create',
        'Update Person': '/person-update/<int:id>',
        'Delete': '/person-delete/<int:id>',
        'List Jobs': '/job-list',
        'Job View': '/job/<int:id>',
        'Create Job': '/job-create',
        'Update Job': '/job-update/<int:id>',
        'Delete Job': '/job-delete/<int:id>',
    }

    return Response(person_api_urls)

# curl -v http://localhost:8000/person_api/person-list/
@api_view(['GET'])
def ShowAll(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

# curl -v http://localhost:8000/person_api/person/3
@api_view(['GET'])
def ShowById(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

# curl -X POST http://localhost:8000/person_api/create-person/ -H 'Content-type:application/json' -d '{"name": "Dan Doe", "age": 20}'
@api_view(['POST'])
def CreatePerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(date_joined = date.today(), date_updated = date.today())
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# curl -X PUT http://localhost:8000/person_api/update-person/3 -H 'Content-type:application/json' -d '{"name": "William Doe", "date_joined": "1920-01-01", "age": 98}'
@api_view(['PUT'])
def UpdatePerson(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save(date_updated = date.today())

    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

# curl -X DELETE http://localhost:8000/person_api/delete-person/5
@api_view(['DELETE'])
def DeletePerson(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response('Person deleted successfully.', status=status.HTTP_204_NO_CONTENT)

# curl -v http://localhost:8000/person_api/job-list/
@api_view(['GET'])
def ShowAllJobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

# curl -v http://localhost:8000/person_api/job/3
@api_view(['GET'])
def ShowJobById(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

# curl -X POST http://localhost:8000/person_api/create-job/ -H 'Content-type:application/json' -d '{"job_title":"Code Tester","salary":3500}'
@api_view(['POST'])
def CreateJob(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# curl -X PUT http://localhost:8000/person_api/update-job/3 -H 'Content-type:application/json' -d '{"job_title":"Batman", "salary":1000000}'
@api_view(['PUT'])
def UpdateJob(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(instance=job, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

# curl -X DELETE http://localhost:8000/person_api/delete-job/5
@api_view(['DELETE'])
def DeleteJob(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return Response('Job deleted successfully.', status=status.HTTP_204_NO_CONTENT)

# curl -X POST http://localhost:8000/person_api/create-job/ -H 'Content-type:application/json' -d '{"job_title":"Nascar Driver","salary":112233}'
# curl -X PUT http://localhost:8000/person_api/create-employee/6 -H 'Content-type:application/json' -d '{"name": "Hannah Doe", "age": 30}'
# Include the id of an existing job in the url to add a job to the newly created person
@api_view(['PUT'])
def CreatePersonWithJob(request, pk):
    job = Job.objects.get(id=pk)
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(job=job)
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        

# curl -X PUT http://localhost:8000/person_api/update-persons-job/3 -H 'Content-type:application/json' -d '{"job_title": "Lifeguard", "salary": 150000}'
# Include the id of a person in the url to update their job with the job in the request
@api_view(['PUT'])
def UpdatePersonsJob(request, pk):
    person = Person.objects.get(id=pk)
    serializer = JobSerializer(data=request.data)
    title = request.data.get('job_title')
    if serializer.is_valid():
        serializer.save()
    person.job = Job.objects.get(job_title=title)
    person.save()
    person = Person.objects.get(id=pk)
    person_serializer = PersonSerializer(person)
    return Response(person_serializer.data, status=status.HTTP_204_NO_CONTENT)