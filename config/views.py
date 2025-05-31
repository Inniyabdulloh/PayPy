from django.shortcuts import redirect

def check_user_is_authenticated(request):
    print(dir(request.user))
    if request.user.is_authenticated:
        return redirect('user:home')
    return redirect('user:sign-in')