from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'card_type',
            'masked_card',
            'last_four',
            'card_holder_name',
            'expiry_month',
            'expiry_year',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']