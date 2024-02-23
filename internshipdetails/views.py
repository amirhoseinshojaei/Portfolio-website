from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Intership
# Create your views here.

def internship (request):

    if not request.user.is_authenticated:
        
        messages.warning (request , "Please login to access to page")
        return redirect ("login")

    if request.method == "POST":

        fname = request.POST.get ("full_name")
        femail = request.POST.get ("email")
        fcollege = request.POST.get ("college_name")
        fnationality = request.POST.get ("nationality")
        fstatus = request.POST.get ("offer_status")
        fstart = request.POST.get ("start_date")
        fend = request.POST.get ("end_date")
        freport = request.POST.get ("proj_report")
        fstamp = request.POST.get ("time_stamp")

        # Converting to upper case
        fname_upper = fname.upper ()
        fcollege_upper = fcollege.upper ()
        fnationality_upper = fnationality.upper ()

        # Check Details
        check1 = internship.objects.filter (full_name = fname)
        check2 = internship.objects.filter (email = femail)
        if check1 or check2 :

            messages.warning (request , "Your Details Are Stored Already")
            return redirect ("home")
        
        query = internship (full_name = fname_upper , email = femail , college_name = fcollege_upper ,
                            nationality = fnationality_upper , offer_status = fstatus , start_date = fstart,
                            end_date = fend , proj_report = freport , timestamp = fstamp)
        query.save()
        messages.success (request , "Form Is Submitted Successful")
        return redirect ("internship")
    return render (request , "internship.html")


