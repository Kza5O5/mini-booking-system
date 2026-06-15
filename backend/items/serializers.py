from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(
        source="created_by.username"
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "created_by",
            "created_at",
        ]