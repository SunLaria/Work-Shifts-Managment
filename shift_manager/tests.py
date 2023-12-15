from django.test import TestCase

# Create your tests here.

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

# Shift.objects.create(Date="2023-06-03",Shift="mo",worker=Worker.objects.all()[0])
# Worker.objects.create(Worker_ID=23223,Full_Name="Sun Laria",Work_Days=6)
