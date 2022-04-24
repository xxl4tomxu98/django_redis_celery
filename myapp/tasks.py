import random
from celery import shared_task
from .models import Sample

@shared_task(name="sum_two_numbers")
def add(x, y):
    x = int(x)
    y = int(y)
    result = Sample.objects.create(value=x+y)   
    return result
	

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    x = int(x)
    y = int(y)
    total = x * (y * random.randint(3, 100))
    result = Sample.objects.create(value=total)
    return result
    

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return Sample.objects.create(value=sum(numbers))
