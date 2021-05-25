from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_joined = models.DateField
    date_updated = models.DateField

    def __str__(self):
        return self.name