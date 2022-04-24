from django.db import models

# Create your models here.


class Sample(models.Model):
	value = models.PositiveIntegerField()

	def __str__(self):
		return str(self.value)