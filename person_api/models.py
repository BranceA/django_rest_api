from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_joined = models.DateField(default='1111-11-11')
    date_updated = models.DateField(default='1111-11-11')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, related_name='job')

    def __str__(self):
        return self.name
