from django import template
from datetime import datetime,date
from shift_manager.models import Shift, Worker
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def list_index(indexable, i):
    return indexable[int(i)]

@register.filter
def list_index_date(indexable, i):
    return "-".join(indexable[int(i)].split("-")[::-1])

@register.filter
def list_split(value):
    return value.split(" ")

@register.simple_tag
def filter_worker_name(date,shift):
    try:
        choice = [i for i in Shift.objects.filter(Date=date,Shift=shift)][0]
        result=f"<option selected value='{choice.Worker.id}'>{choice.Worker.Full_Name}</option>"
        return mark_safe(result)
    except:
        return ""

