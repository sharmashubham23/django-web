from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def account(request):
    return render(request, 'account/accounthome.html')


def handelSingup(request):
    if request.method == "POST":
        # GET POST PARAMETERS
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # check for error inputs
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/shop')
        if not username.isalnum():
            messages.error(
                request, "Username must contains characters and numbers only.")
            return redirect('/shop')
        if pass1 != pass2:
            messages.error(request, "Password does not match")
            return redirect('/shop')

        #  Creat the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account is Successfully created.")
        return redirect('/shop')

    else:
        return HttpResponse("404 - Page Not Found")


def handelLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, "Successfuly Logged In")
            return redirect('/shop/')
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid Credentials, please try again")
            return redirect('/shop/')

    return HttpResponse("404 - Page Not Found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfuly Logged Out")
    return redirect('/shop/')
