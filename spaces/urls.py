from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    JoinSpace,
    LeaveSpace,
    CreateSpace
)

urlpatterns = [
    path("home/", HomeView.as_view(), name="homepage"),
    path("joinspace/<int:pk>/", JoinSpace.as_view(), name="joinspace"),
    path("leavespace/<int:pk>/", LeaveSpace.as_view(), name="leavespace"),
    path("create-space/", CreateSpace.as_view(), name="createspace"),
]
