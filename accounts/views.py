from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        # User have data and want an account now
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists!!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must be same!!'})

    else:
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # TODO need to route to homepage
    # and don't forget to logout
    return render(request, 'accounts/signup.html')
