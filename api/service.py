from card import service as card_service, models as card_model


def get_card_with_id(card_id: int):
    try:
        card = card_model.Card.objects.get(id=card_id)
    except:
        return False
    return card

