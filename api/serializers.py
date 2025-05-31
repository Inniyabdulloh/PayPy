from rest_framework import serializers
from card import models

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ['first_name', 'last_name', 'number', 'year', 'month', 'balance']


class MakeTransactionSerializer(serializers.Serializer):
    from_card = serializers.IntegerField()
    to_card = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class DetailTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ['from_card', 'to_card', 'amount', 'status', 'time_transaction']