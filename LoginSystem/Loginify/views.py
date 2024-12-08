from django.shortcuts import render, redirect
from .models import UserDetail
from django.http import HttpResponse
from .forms import SignupForm, LoginForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = UserDetail.objects.create(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password")
            )
            return JsonResponse({"message": "User created successfully!", "user_id": user.username}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
def get_all_users(request):
    if request.method == "GET":
        users = list(UserDetail.objects.values("username", "email"))
        return JsonResponse({"users": users}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
def get_user(request, username):
    if request.method == "GET":
        try:
            user = UserDetail.objects.get(username=username)
            return JsonResponse({
                "username": user.username,
                "email": user.email
            }, status=200)
        except UserDetail.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
def update_user(request, username):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            user = UserDetail.objects.get(username=username)
            user.email = data.get("email", user.email)
            user.password = data.get("password", user.password)
            user.save()
            return JsonResponse({"message": "User updated successfully!"}, status=200)
        except UserDetail.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
def delete_user(request, email):
    if request.method == "DELETE":
        try:
            user = UserDetail.objects.get(email=email)
            user.delete()
            return JsonResponse({"message": "User deleted successfully!"}, status=200)
        except UserDetail.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=405)