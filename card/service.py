from decimal import Decimal
from . import models, utils, forms
from django.db import transaction
from user.models import Token


def create_card(first_name: str, last_name: str, user: models.CustomUser = None):
    card_data = {
        "first_name": first_name,
        "last_name": last_name,
        "number": next(utils.card),
        "year": utils.generate_expiry_year(),
        "month": utils.generate_expiry_month(),
    }

    if user:
        card_data["user"] = user

    return models.Card.objects.create(**card_data)

def get_card_list_user(user: models.CustomUser):
    try:
        return models.Card.objects.filter(user=user)
    except:
        return False

def get_user_card(user: models.CustomUser, card_id: int):
    try:
        return models.Card.objects.get(user=user, id=card_id)
    except:
        return False

def get_card_with_card_number(card_number: int):
    try:
        return models.Card.objects.get(number=card_number)
    except:
        return False

def make_transaction(from_card: models.Card, to_card: models.Card, token:str, amount: float) -> models.Transaction:
    if from_card == to_card:
        raise ValueError("Cannot transfer to the same card.")

    if from_card.balance < amount:
        raise ValueError("Insufficient funds.")

    tx = models.Transaction.objects.create(
        from_card=from_card,
        to_card=to_card,
        amount=amount,
        token=check_token(token),
        status='pending'
    )

    try:
        with transaction.atomic():
            sender = models.Card.objects.select_for_update().get(id=from_card.id)
            receiver = models.Card.objects.select_for_update().get(id=to_card.id)

            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()
            tx.status = 'complated'
            tx.save()
    except:
        tx.status = 'failed'
        tx.save()

    return tx

def add_free_money_to_card_from_paypy(card: models.Card):
    try:
        card.balance += Decimal("1000000.00")
        card.save()
        return True
    except:
        return False


def edit_card(form: forms.EditCardForm):
    if form.is_valid():
        form.save()

def switch_status_of_card(user, card):
    if card.user.id == user.id:
        if card.status:
            card.status = False
        else:
            card.status = True
        card.save()

def check_token(token: str):
    try:
        key = Token.objects.get(key=token)
    except:
        return False
    return key