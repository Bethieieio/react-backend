from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'created_at', 'owner', 'post'
        ]

    def create(self, validated_error):
        try:
            return super().create(validated_error)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible deplicate'
            })
