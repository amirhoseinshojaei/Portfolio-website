from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
# Create your views here.

def signup (request):

    if request.method=='POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        get_confirm_password = request.POST.get('pass2')

        if get_password!= get_confirm_password :
            messages.info (request , 'Password is not matching')
            return redirect ('signup')
        
        try:

            if User.objects.get(username=get_email):

                messages.warning (request , "Email is taken")
                return redirect ('signup')
            
        except Exception as identifier:
            pass

        my_user = User.objects.create_user (get_email,get_password)
        my_user.save()
        my_user = authenticate (username = get_email , password = get_password)

        if my_user is not None:

            login (request,my_user)
            messages.success (request , "Login Success")
            return redirect ('home')
        else:
            messages.error(request, 'invalid Credentials')

    return render (request , 'signup.html')

def login (request):

    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        my_user = authenticate (username = get_email , password = get_password)

        if my_user is not None:
            login (request , my_user)
            messages.success (request , 'Login Success')
            return redirect ('home')
        else:
            messages.error (request , 'Invalid Credentials')

    return render (request , 'login.html')

def logout (request):

    logout (request)
    messages.success (request , 'logout success')
    return redirect ('home')


