import random
import string

store = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_url_data(code):
    return store.get(code)
