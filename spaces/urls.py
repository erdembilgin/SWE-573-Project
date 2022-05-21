from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    JoinSpace,
    LeaveSpace
)

urlpatterns = [
    path("home/", HomeView.as_view(), name="homepage"),
    path("joinspace/<int:pk>/", JoinSpace.as_view(), name="joinspace"),
    path("leavespace/<int:pk>/", LeaveSpace.as_view(), name="leavespace"),
]
