from django.shortcuts import render, redirect
from .models import UserDetail
from django.http import HttpResponse
from .forms import SignupForm, LoginForm


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, "Loginify/signup.html", {'form': form})


def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UserDetail.objects.filter(email=email, password=password).first()
            if user:
                message = "Login Successful!"
            else:
                message = "Invalid credentials!"
    else:
        form = LoginForm()
    return render(request, 'Loginify/login.html', {'form': form, 'message': message})