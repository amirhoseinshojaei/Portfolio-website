from django.urls import path
from .import views
# Create urls here

urlpatterns = [
    path ('signup',views.signup, name= 'signup'),
]