from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('new_index')  # Replace 'index' with your home page URL
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # messages.success(request, "Registration successful")
                return redirect('credentials:login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('credentials:register')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')  # Replace 'index' with the actual URL name for your home page
