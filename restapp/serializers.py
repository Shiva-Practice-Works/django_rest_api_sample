from rest_framework import serializers
from .models import EmployeeDetails

class EmployeeDetailsSerailizer(serializers.ModelSerializer):
	class Meta:
		 model = EmployeeDetails
		 fields = '__all__'