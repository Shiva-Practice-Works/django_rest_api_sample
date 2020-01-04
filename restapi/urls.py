from django.contrib import admin
from django.urls import path, include
from restapp.views import EmployeeDetailsViewSet, EmployeeDetailsViewsSet2
from restapp.views2 import (get_details, 
	                   post_object_details, put_object, delete_object, get_single_object)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/emp/', EmployeeDetailsViewSet.as_view()),
    path('api/v1/emp/<int:pk>/', EmployeeDetailsViewsSet2.as_view()),


    path('api/v2/emp/get/', get_details),
    path('api/v2/emp/post/', post_object_details),
    path('api/v2/emp/put/<int:pk>/', put_object),
    path('api/v2/emp/object/<int:pk>/', get_single_object),
    path('api/v2/emp/delete/<int:pk>/', delete_object)
]
