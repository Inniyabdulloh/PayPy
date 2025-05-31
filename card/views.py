from . import service, forms

from user import service as user_service
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect


class CardCreateView(View, LoginRequiredMixin):
    def get(self, request):
        user = user_service.get_user_from_db(request)
        card = service.create_card(first_name='ismoil', last_name='mamirov', user=user)

        return redirect('user:home')


class CardListView(View, LoginRequiredMixin):
    def get(self, request):
        user = user_service.get_user_from_db(request)
        context = {
            'card_list_user': service.get_card_list_user(user=user)
        }

        return render(request, 'card/card-list.html', context)


class CardDetailView(View, LoginRequiredMixin):
    def get(self, request, card_id):
        user = user_service.get_user_from_db(request)
        context = {
            'card': service.get_user_card(user=user, card_id=card_id)
        }
        return render(request, 'card/card-detail.html', context)


class CardEditView(View, LoginRequiredMixin):
    def post(self, request, card_id):
        user = user_service.get_user_from_db(request)
        card = service.get_user_card(user=user, card_id=card_id)
        form = forms.EditCardForm(data=request.POST, instance=card)
        service.edit_card(form)

        return redirect('card:card-detail', card.id)


class SwitchStatusOfCard(View, LoginRequiredMixin):
    def get(self, request, card_id):
        user = user_service.get_user_from_db(request)
        card = service.get_user_card(user=user, card_id=card_id)
        service.switch_status_of_card(user=user, card=card)

        return redirect('card:card-list')