from . import forms, service, models
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

class HomePageView(View, LoginRequiredMixin):
    def get(self, request):
        return render(request, 'user/home.html')


class UserRegisterView(View):
    def get(self, request):
        return  render(request, 'user/sign-up.html')

    def post(self, request):
        form = forms.UserRegisterForm(request.POST)
        user = service.create_user(form)
        print(user)
        if user:
            return redirect('user:sign-in')
        return redirect('user:sign-up')

class UserLoginView(View):
    def get(self, request):
        return render(request, 'user/sign-in.html')

    def post(self, request):
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('user:home')
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri")
            return render(request, 'user/sign-in.html')


class TokenListView(View, LoginRequiredMixin):
    def get(self, request):
        token_list = service.get_user_tokens(request.user)
        return render(request, 'user/token-list.html', {'token_list': token_list})


class CreateTokenView(View, LoginRequiredMixin):
    def post(self, request):
        form = forms.CreateTokenForm(data=request.POST)
        service.create_token(form=form, user=request.user)
        return redirect('user:token-list')


class SwitchStatusOfTokenView(View, LoginRequiredMixin):
    def get(self, request, id):
        token = service.get_user_token(id=id)
        service.switch_status_of_token(user=request.user, token=token)
        return redirect('user:token-list')