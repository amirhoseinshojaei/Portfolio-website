from django.shortcuts import render
from .models import Service
# Create your views here.
# TODO ; create view for service and complete app team

def service_list (request):

    service = Service.objects.all()
    context = {
        'posts': service
    }
    return render (request , 'service.html', context)