from datetime import datetime
from . import models

def generate_card_number() -> str:
    card_num = 4231201002482000

    while True:
        card_from_db = models.Card.objects.latest('id').number
        if card_from_db:
            card_num = int(card_from_db)
        card_num += 1
        yield card_num

def generate_expiry_year() -> str:
    future_year = datetime.now().year + 3
    return str(future_year)[-2:]

def generate_expiry_month() -> str:
    return f"{datetime.now().month:02}"


card = generate_card_number()


