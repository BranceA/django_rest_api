from django.test import TestCase

from .models import Person, Job

class PersonTest(TestCase):
    # Test for person model
    def setUp(self):
        Person.objects.create(age=30, date_joined='2021-05-10', date_updated='2021-05-15', name='Bob Doe')
        Person.objects.create(age=45, date_joined='2021-05-02', date_updated='2021-05-15', name='Sally Doe')
        Person.objects.create(age=7, date_joined='2021-08-10', date_updated='2021-11-10', name='Billy Doe')
        Person.objects.create(age=22, date_joined='2020-02-10', date_updated='2021-12-25', name='Bertha Doe')

    def test_person_name(self):
        bob = Person.objects.get(name='Bob Doe')
        sally = Person.objects.get(name='Sally Doe')
        self.assertEqual(bob.name, 'Bob Doe')
        self.assertEqual(sally.name, 'Sally Doe')