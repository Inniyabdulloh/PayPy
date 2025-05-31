from decimal import Decimal
from django.db import models
from user.models import CustomUser, Token


class Card(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    number = models.CharField(max_length=16)
    year = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00')  )
    status = models.BooleanField(default=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='card')



class Transaction(models.Model):
    from_card = models.ForeignKey(Card, on_delete=models.RESTRICT, related_name='sent_transactions')
    to_card = models.ForeignKey(Card, on_delete=models.RESTRICT, related_name='received_transactions')
    token = models.ForeignKey(Token, on_delete=models.RESTRICT, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ])
    time_transaction = models.DateTimeField(auto_now_add=True)
