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
   Worker = models.ForeignKey(Worker,on_delete=models.CASCADE, choices=[(str(i.id), str(i.Full_Name)) for i in Worker.objects.all()])


# class WorkerForm(forms.Form):
#     class Meta:
#         model = Worker
#         fields = ["Worker_ID", "Full_Name", "Work_Days"]

# class Shift(forms.Form):
#     class Meta:
#         model = Shift
#         fields = ["Date", "Shift", "Worker"]


# q.get_Shift_display() - מראה את הבחירה בצורה המלאה לפי ה choices
# q.clean_fields() - בודק את כל הפרמרטרים עם validators

# Worker.objects.create(Worker_ID=23223,Full_Name="Sun Laria",Work_Days=6)
