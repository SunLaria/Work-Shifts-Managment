from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django import forms



class Worker(models.Model):
    Worker_ID = models.IntegerField(validators=[MinValueValidator(10000),MaxValueValidator(99999)])
    Full_Name = models.CharField(max_length=20)
    Work_Days = models.IntegerField()
    


class Shift(models.Model):
    Date = models.DateField("shift date")
    Shift = models.CharField(max_length=10, choices=[("mo","Morning"),("af","Afternoon"),("ni","Night")])
    Worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
