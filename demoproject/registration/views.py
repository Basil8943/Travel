from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from registration.models import form


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid  username or password")
            return redirect('login')
    return render(request,"login.html")
    return render(request,"login.html")
def register(request):
    img=form.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exist")
                print("user exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=name,email=email)
                user.save()
                messages.info(request,"user created")
                return redirect('login')
        else:
            messages.info(request,"check password")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html",{'reg': img})

def logout(request):
    auth.logout(request)
    return redirect('/')















def reg(request):
    return render(request,"test.html")
