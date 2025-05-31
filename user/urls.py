from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('documentation/', views.DocumentationView.as_view(), name='documentation'),
    path('sign-up/', views.UserRegisterView.as_view(), name='sign-up'),
    path('sign-in/', views.UserLoginView.as_view(), name='sign-in'),
    path('logout/', views.UserLoguotView.as_view(), name='logout'),
    path('token-list/', views.TokenListView.as_view(), name='token-list'),
    path('token-create/', views.CreateTokenView.as_view(), name='token-create'),
    path('token-switch/<int:id>/', views.SwitchStatusOfTokenView.as_view(), name='token-switch')
]