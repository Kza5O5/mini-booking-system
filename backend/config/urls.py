from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    home,
    health_check,
)

urlpatterns = [
    path("", home, name="home"),

    path(
        "health/",
        health_check,
        name="health",
    ),

    path(
        "api/",
        include("users.urls"),
    ),

    path(
        "api/",
        include("items.urls"),
    ),

    path(
        "api/login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path(
        "admin/",
        admin.site.urls,
    ),
]