from django.db import models


class EmployeeDetails(models.Model):
	e_name = models.CharField(max_length = 50)
	e_number = models.IntegerField()
	e_email = models.EmailField()
	def __str__(self):
		return self.e_name