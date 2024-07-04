from django.contrib import admin
from django.urls import path
from account.views import UserLoginView, UserRegistrationView, UserProfileView, UserChangePasswordView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
