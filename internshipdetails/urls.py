from django.urls import path
from . import views
# Create urls here

urlpatterns = [
    path ("form/",views.internship,name= 'internship'),
]