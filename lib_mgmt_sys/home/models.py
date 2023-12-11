from statistics import mode
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length= 100)
    roll = models.IntegerField()

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    is_present = models.BooleanField(default=True)
    salary = models.FloatField()

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name


class AuthorPenName(models.Model):
    name = models.CharField(max_length=150)
    awards = models.CharField(max_length=100)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.name