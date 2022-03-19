from xml.dom.minidom import CharacterData
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.PositiveIntegerField(unique=True)
    email = models.CharField(max_length=255)
    birth_date = models.DateField()


class Performance_Forms(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    study_hours = models.PositiveIntegerField()
    total_questions = models.PositiveIntegerField()
    total_scores = models.PositiveIntegerField()
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)

    
class Mental_Forms(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    energy_level = models.IntegerField(blank=True, null=True)
    mental_state = models.CharField(max_length=255, blank=True, null=True)
    acidity_level = models.CharField(max_length=255, blank=True, null=True)
    day_going = models.CharField(max_length=255, blank=True, null=True)
    feeling = models.CharField(max_length=255, blank=True, null=True)


class Activities_Types(models.Model):
    activity_type = models.CharField(max_length=255)
    importance_level = models.CharField(max_length=255)

