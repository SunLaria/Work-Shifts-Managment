from django import template
from datetime import datetime,date

register = template.Library()

@register.filter
def list_index(indexable, i):
    return indexable[int(i)]

@register.filter
def list_index_date(indexable, i):
    date_result=tuple(map(int,indexable[int(i)].split("-")))[::-1]
    return date(date_result[0],date_result[1],date_result[2]).strftime('%Y-%m-%d')

@register.filter
def list_split(value):
    return value.split(" ")


# date(date[2],date[1],date[0]).strftime('%Y-%m-%d')
# datetime.date(2023,12,14).strftime('%d-%m-%Y')