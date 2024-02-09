from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(name, email, pass1, pass2)

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # Split the name into first name and last name
            name_parts = name.split()
            first_name = ' '.join(name_parts[:-1]) if len(name_parts) > 1 else name_parts[0]
            last_name = name_parts[-1] if len(name_parts) > 1 else ''

            my_user = User.objects.create_user(email, email, pass1, first_name=first_name, last_name=last_name)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')
        

def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=email,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')