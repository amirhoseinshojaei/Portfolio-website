from django.shortcuts import render , get_object_or_404
from .models import Service
# Create your views here.
# TODO ; create view for service and complete app team

def service_list (request):

    service = Service.objects.all()
    context = {
        'posts': service
    }
    return render (request , 'service.html', context)

def service_detail (request , id):

    service = get_object_or_404 (Service , pk = id)
    context = {
        'post':service
    }
    return render (request , 'service_detail.html', context)