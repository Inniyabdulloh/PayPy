from django.db import models
from user.models import CustomUser


class Card(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    number = models.CharField(max_length=16)
    year = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class UserCard(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='user')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cards')


class Transaction(models.Model):
    from_card = models.ForeignKey(Card, on_delete=models.RESTRICT, related_name='sent_transactions')
    to_card = models.ForeignKey(Card, on_delete=models.RESTRICT, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_transaction = models.DateTimeField()
