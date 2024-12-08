from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create-user/', views.create_user, name='create_user'),
    path('get-all-users/', views.get_all_users, name='get_all_users'),
    path('get-user/<str:username>/', views.get_user, name='get_user'),
    path('update-user/<str:username>/', views.update_user, name='update_user'),
    path('delete-user/<str:email>/', views.delete_user, name='delete_user'),
]