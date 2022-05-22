from django.contrib import admin
from django.urls import path, include
from .views import (
    index,
    LoginView,
    LogoutView,
    RegisterView,
    Profile,
    ChangePassword
)

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("sign-up/", RegisterView.as_view(), name="signup"),
    path("profile/", Profile.as_view(), name="profile"),
    path("change-password/", ChangePassword.as_view(), name="change_password"),
]
