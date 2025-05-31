from django import template

register = template.Library()

@register.filter
def format_card_number(card):
    return ' '.join([card[i:i+4] for i in range(0, len(card), 4)])