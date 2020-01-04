from rest_framework.decorators import api_view
from .models import EmployeeDetails
from .serializers import EmployeeDetailsSerailizer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', ])
def get_details(request):
    if request.method == 'GET':
       query = EmployeeDetails.objects.all()
       serializer = EmployeeDetailsSerailizer(query, many = True)
       return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(serializer.error, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST', ])
def post_object_details(request):
	if request.method == 'POST':
		serializer = EmployeeDetailsSerailizer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
	return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
def put_object(request, pk):
	if request.method == 'PUT':
		query = EmployeeDetails.objects.get(pk = pk)
		serializer = EmployeeDetailsSerailizer(query, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
	return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def delete_object(request, pk):
	if request.method == 'DELETE':
		query = EmployeeDetails.objects.get(pk = pk)
		query.delete()
		return Response(status.HTTP_204_NO_CONTENT)
	return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_single_object(request,pk):
	if request.method == 'GET':
		query = EmployeeDetails.objects.get(pk = pk)
		serializer = EmployeeDetailsSerailizer(query)
		return Response(serializer.data, status = status.HTTP_200_OK)