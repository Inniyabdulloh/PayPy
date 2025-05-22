import uuid

def generate_token(length=15):
    return uuid.uuid4().hex[:length]