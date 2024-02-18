from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog (request):

    blogs = Blog.objects.all()
    context = {
        'posts':blogs
    }
    return render (request , 'blogs.html', context)