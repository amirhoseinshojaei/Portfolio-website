from django.shortcuts import render , get_object_or_404
from .models import Blog
# Create your views here.

def blog (request):

    blogs = Blog.objects.all()
    context = {
        'posts':blogs
    }
    return render (request , 'blogs.html', context)

def blog_detail(request,id):
    
    blog = get_object_or_404 (Blog , pk = id)
    context = {
        'post':blog
    }
    return render (request , 'blog-detail.html', context)
