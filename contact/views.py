from django.shortcuts import render , redirect
from django.contrib import messages
from . models import Contact
# Create your views here.

def contact (request):

    if request.method == "POST":

        fname = request.POST.get ("name")
        femail = request.POST.get ("email")
        fphone = request.POST.get ("phone")
        fmessage = request.POST.get ("message")
        query = contact (name = fname , email = femail , phone = fphone , message = fmessage)
        query.save()
        messages.success (request , "Thanks for contacting us. We will get by you Soon")
        return redirect ("home")
    return render (request , 'contact.html')