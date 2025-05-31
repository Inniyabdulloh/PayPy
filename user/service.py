from . import forms, utils, models
from django.http import HttpRequest

def get_user_from_db(request: HttpRequest):
    return models.CustomUser.objects.get(id=request.user.id)

def create_user(form: forms.UserRegisterForm):
    if form.is_valid():
        form.save()
        return form
    return False


def create_token(form: forms.CreateTokenForm, user: models.CustomUser):
    if form.is_valid():
        models.Token.objects.create(
            name=form.cleaned_data['name'],
            key=utils.generate_token(),
            user=user
        )

        return True
    return False

def get_user_tokens(user: models.CustomUser):
    return models.Token.objects.filter(user=user.id)

def get_user_token(id: int):
    return models.Token.objects.get(id=id)

def switch_status_of_token(user, token):
    if token.user.id == user.id:
        if token.status:
            token.status = False
        else:
            token.status = True
        token.save()


