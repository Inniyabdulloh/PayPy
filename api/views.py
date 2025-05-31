from . import serializers, service
from card import service as card_service
from rest_framework.views import APIView, Response

# Create your views here.

class CardDetailApiView(APIView):
    def get(self, request, token, card_id):
        card = service.get_card_with_id(card_id)

        if card is False:
            return Response({'error': "Card does not exist"})
        serializer = serializers.CardSerializer(card)
        return Response(serializer.data)


class MakeTransactionsApiView(APIView):
    def post(self, request, token):
        serializer = serializers.MakeTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        from_card = card_service.get_card_with_card_number(data.get('from_card'))
        to_card = card_service.get_card_with_card_number(data.get('to_card'))
        amount = data.get('amount')

        if from_card is False:
            return Response({'error': "Sender card does not found"})

        if to_card is False:
            return Response({'error': "Receiving card does not found"})

        transaction_result = card_service.make_transaction(from_card, to_card, token, amount)
        detail_transaction_serializer = serializers.DetailTransactionSerializer(transaction_result)
        return Response(detail_transaction_serializer.data)


class AddFreeMoneyToCard(APIView):
    def get(self, request, token, card_number):
        card = card_service.get_card_with_card_number(card_number)
        if card:
            added_money = card_service.add_free_money_to_card_from_paypy(card)

            if added_money:
                return Response({'status':'ok'})
            return Response({'error': "server error"})


        return Response({"error": f"Does not exist card with id {card_number}"})


