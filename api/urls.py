from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('<str:token>/card/detail/<int:card_id>/', views.CardDetailApiView.as_view(), name='card-detail'),
    path('<str:token>/card/transaction/', views.MakeTransactionsApiView.as_view(), name='card-transaction'),
    path('<str:token>/card/free-money/<int:card_id>/', views.AddFreeMoneyToCard.as_view(), name='free-money'),
]

