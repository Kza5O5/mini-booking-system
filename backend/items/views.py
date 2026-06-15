from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Item
from .serializers import ItemSerializer


class ItemListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
        )


class ItemDeleteView(
    generics.DestroyAPIView
):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(
            created_by=self.request.user
        )