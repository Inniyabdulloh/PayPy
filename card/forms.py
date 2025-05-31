from . import models
from django.forms import ModelForm

class EditCardForm(ModelForm):
    class Meta:
        model = models.Card
        fields = ['first_name', 'last_name']