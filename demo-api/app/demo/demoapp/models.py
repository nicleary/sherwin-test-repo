from django.db import models

# Create your models here.


class Cat(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(null=False, max_length=64)
    breed = models.CharField(null=False, max_length=32)
    age = models.IntegerField(null=False)


class Dog(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(null=False, max_length=64)
    breed = models.CharField(null=False, max_length=32)
    age = models.IntegerField(null=False)
