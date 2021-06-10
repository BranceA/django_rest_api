import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import datetime

from .models import Person, Job
from .serializers import PersonSerializer, JobSerializer

client = Client()

class PersonTest(TestCase):
    # Test for person model
    def setUp(self):
        clown = Job.objects.create(job_title='Circus Clown', salary=35000)
        doctor = Job.objects.create(job_title='Doctor', salary=120000)
        realtor = Job.objects.create(job_title='Realtor', salary=62000)
        professor = Job.objects.create(job_title='Professor', salary=50000)

        Person.objects.create(age=30, date_joined='2021-05-10', date_updated='2021-05-15', name='Bob Doe', job=clown)
        Person.objects.create(age=45, date_joined='2021-05-02', date_updated='2021-05-15', name='Sally Doe', job=doctor)
        Person.objects.create(age=7, date_joined='2021-08-10', date_updated='2021-11-10', name='Billy Doe', job=realtor)
        Person.objects.create(age=22, date_joined='2020-02-10', date_updated='2021-12-25', name='Bertha Doe', job=professor)

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

    # def test_get_all_people(self):
    #     # get API response
    #     response = client.get(reverse('ShowAll'))
    #     # get data from db
    #     people = Person.objects.all()
    #     serializer = PersonSerializer(people, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)