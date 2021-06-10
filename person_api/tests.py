import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
import datetime

from .models import Person, Job
from .serializers import PersonSerializer, JobSerializer

class PersonTest(TestCase):
    # Test for person model
    def setUp(self):
        self.client = Client()
        self.clown = Job.objects.create(job_title='Circus Clown', salary=35000)
        self.doctor = Job.objects.create(job_title='Doctor', salary=120000)
        self.realtor = Job.objects.create(job_title='Realtor', salary=62000)
        self.professor = Job.objects.create(job_title='Professor', salary=50000)

        self.bob = Person.objects.create(age=30, date_joined='2021-05-10', date_updated='2021-05-15', name='Bob Doe', job=self.clown)
        self.sally = Person.objects.create(age=45, date_joined='2021-05-02', date_updated='2021-05-15', name='Sally Doe', job=self.doctor)
        self.billy = Person.objects.create(age=7, date_joined='2021-08-10', date_updated='2021-11-10', name='Billy Doe', job=self.realtor)
        self.bertha = Person.objects.create(age=22, date_joined='2020-02-10', date_updated='2021-12-25', name='Bertha Doe', job=self.professor)

        self.dan = {
            'name': 'Dan Doe',
            'age': 20
        }
        self.william = {
            "name": "William Doe", 
            "date_joined": "1920-01-01", 
            "age": 98
        }
    # Test for person model
    def test_person(self):
        bob = Person.objects.get(name='Bob Doe')
        sally = Person.objects.get(name='Sally Doe')
        billy = Person.objects.get(name='Billy Doe')
        bertha = Person.objects.get(name='Bertha Doe')
        # test name has been created correctly
        self.assertEqual(bob.name, 'Bob Doe')
        self.assertEqual(sally.name, 'Sally Doe')
        # test age has been created correctly
        self.assertEqual(billy.age, 7)
        self.assertEqual(bertha.age, 22)
        # test date joined has been created correctly
        self.assertEqual(sally.date_joined, datetime.date(2021, 5, 2))
        self.assertEqual(bertha.date_joined, datetime.date(2020, 2, 10))
        # test date updated has been created correctly
        self.assertEqual(bob.date_updated, datetime.date(2021, 5, 15))
        self.assertEqual(billy.date_updated, datetime.date(2021, 11, 10))
        # test to see if job is added correctly
        self.assertEqual(sally.job.job_title, 'Doctor')
        self.assertEqual(sally.job.salary, 120000)
        self.assertEqual(billy.job.job_title, 'Realtor')
        self.assertEqual(billy.job.salary, 62000)

    # test to see if get request gets list of all people
    def test_get_all_people(self):
        # get API response
        response = self.client.get(reverse('person-list'))
        # get data from db
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test to see if a single person can be gotten successfully
    def test_get_valid_single_person(self):
        response = self.client.get(
            reverse('single-person', kwargs={'pk': self.billy.pk}))
        person = Person.objects.get(pk=self.billy.pk)
        serializer = PersonSerializer(person)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test to check if person can be created
    def test_create_person(self):
        response = self.client.post(
            reverse('create-person'),
            data=json.dumps(self.dan),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test to check if person can be updated
    def test_update_person(self):
        response = self.client.put(
            reverse('update-person', kwargs={'pk': self.billy.pk}),
            data=json.dumps(self.william),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)