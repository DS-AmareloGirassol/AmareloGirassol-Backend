import string
import random


def generate_random_password():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(20))

def create_token_response(token, user_id, user_email, user_name):
    response = {
            'token': token,
            'user': {
                'id': user_id,
                'email': user_email,
                'name': user_name,
            }
        }

    return response

def create_valid_token_response(is_valid_token):
    response = {
        'is_valid_token': is_valid_token
    }

    return response