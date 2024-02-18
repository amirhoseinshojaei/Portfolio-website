from django.urls import path
from . import views
# Create urls here

urlpatterns = [
    path ('', views.blog, name= 'blogs'),
    path ('<int:id>', views.blog_detail, name='blog-detail'),
]