from django.urls import path
from . import views
# Create urls here

urlpatterns = [
    path ("",views.service_list, name="service_list"),
    path ("<int:pk>", views.service_detail , name= 'service_detail'),
]