from . import views
from django.urls import path

app_name = 'card'


urlpatterns = [
    path('create/', views.CardCreateView.as_view(), name='card-create'),
    path('list/', views.CardListView.as_view(), name='card-list'),
    path('<int:card_id>/detail/', views.CardDetailView.as_view(), name='card-detail'),
    path('<int:card_id>/edit/', views.CardEditView.as_view(), name='card-edit'),
    path('<int:card_id>/switch-status/', views.SwitchStatusOfCard.as_view(), name='switch-status'),
]