from django.urls import path

from .views import (
    ItemListCreateView,
    ItemDeleteView,
)

urlpatterns = [
    path(
        "items/",
        ItemListCreateView.as_view(),
        name="items",
    ),

    path(
        "items/<int:pk>/",
        ItemDeleteView.as_view(),
        name="delete-item",
    ),
]