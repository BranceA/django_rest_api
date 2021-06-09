from django.test import TestCase
from . .models import Person, Job

class PersonTest(TestCase):
    # Test for person model
    def setUp(self):
        Person.objects.create(age=30, date_joined='2021-05-10', date_updated='2021-05-15', name='Bob Doe')
        Person.objects.create(age=45, date_joined='2021-05-02', date_updated='2021-05-15', name='Sally Doe')
        Person.objects.create(age=7, date_joined='2021-08-10', date_updated='2021-11-10', name='Billy Doe')
        Person.objects.create(age=22, date_joined='2020-02-10', date_updated='2021-12-25', name='Bertha Doe')