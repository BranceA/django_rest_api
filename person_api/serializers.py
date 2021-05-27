from rest_framework import serializers, fields

from . models import Job, Person

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=False)
    class Meta:
        model = Person
        fields = '__all__'
