from django.urls import path
from . import views
# create urls here

urlpatterns = [
    path ("",views.home , name= 'home'),
]