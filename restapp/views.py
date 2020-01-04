from django.shortcuts import render
from .serializers import EmployeeDetailsSerailizer
from .models import EmployeeDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class EmployeeDetailsViewSet(APIView):
     def get(self, request, format=None):
            queryset = EmployeeDetails.objects.all()
            serializer = EmployeeDetailsSerailizer(queryset, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
         
     def post(self, request, format=None):
        serializer = EmployeeDetailsSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailsViewsSet2(APIView):
   def get_object(self, pk):
       try:
            return EmployeeDetails.objects.get(pk=pk)
       except EmployeeDetails.DoesNotExist:
            raise Http404

   def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = EmployeeDetailsSerailizer(queryset)
        return Response(serializer.data)

   def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = EmployeeDetailsSerailizer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
