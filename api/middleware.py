import re
from django.http import JsonResponse
from user.models import Token

class TokenCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            path = self.extract_token_from_path(request.path)
            if len(path) == 15 and self.is_valid_token(path):
                return self.get_response(request)
            return JsonResponse({'error': f"Token ({path}) does not exist"})
        return self.get_response(request)

    def is_valid_token(self, token):
        try:
            token = Token.objects.get(key=token)
            return token.status
        except:
            return False

    def extract_token_from_path(self, request_path):
        match = re.match(r'^/api/([^/]+)/', request_path)
        if match:
            return match.group(1)
        return None


