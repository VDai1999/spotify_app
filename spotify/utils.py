import random
import string

def generate_random_username(length=26):
        characters = string.ascii_letters + string.digits  # Include both letters and digits
        username = ''.join(random.choice(characters) for _ in range(length))
        
        return username