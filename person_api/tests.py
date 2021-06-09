from django.test import TestCase
import datetime

from .models import Person, Job

class PersonTest(TestCase):
    # Test for person model
    def setUp(self):
        Person.objects.create(age=30, date_joined='2021-05-10', date_updated='2021-05-15', name='Bob Doe')
        Person.objects.create(age=45, date_joined='2021-05-02', date_updated='2021-05-15', name='Sally Doe')
        Person.objects.create(age=7, date_joined='2021-08-10', date_updated='2021-11-10', name='Billy Doe')
        Person.objects.create(age=22, date_joined='2020-02-10', date_updated='2021-12-25', name='Bertha Doe')

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