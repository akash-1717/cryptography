import hashlib
import random
import string


def create_password_file(num_passwords):
    passwords = []

    for _ in range(num_passwords):
        password = generate_random_password()
        passwords.append(password)
    
    return passwords


def generate_random_password():
    password_length = random.randint(8, 12)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    
    return password


def compute_hash(password, salt=None):
    if salt:
        password = salt + password

    hash_value = hashlib.md5(password.encode()).hexdigest()
    return hash_value


def save_passwords_with_hashes(passwords, salt=None):
    password_hashes = {}

    for password in passwords:
        hash_value = compute_hash(password, salt)
        password_hashes[password] = hash_value
    
    return password_hashes


def authenticate_password(password, password_hashes, salt=None):
    if password in password_hashes:
        stored_hash = password_hashes[password]
        computed_hash = compute_hash(password, salt)

        return stored_hash == computed_hash
    
    return False


num_passwords = 10
passwords = create_password_file(num_passwords)
print("Passwords:", passwords)

password_hashes = save_passwords_with_hashes(passwords)
print("Password Hashes:", password_hashes)

salt = "somesalt"
salted_password_hashes = save_passwords_with_hashes(passwords, salt)
print("Salted Password Hashes:", salted_password_hashes)

password_to_authenticate = passwords[3]
print("\nPassword to Authenticate:", password_to_authenticate)

authenticated = authenticate_password(password_to_authenticate, password_hashes)
print("Authenticated (without salt):", authenticated)

authenticated_with_salt = authenticate_password(password_to_authenticate, salted_password_hashes, salt)
print("Authenticated (with salt):", authenticated_with_salt)

# Output:
# Passwords: ['9TQ7cwN', 'yDXm7VfJmN', '8TZU7Fn2B', 'D53Ne9gN', '86F83aE', 'A7JUZfx6hX', 'wV6gDpLjW', 'enQxJ3p4', 'Pjp7cKPw', '95tYZTN9']
# Password Hashes: {'9TQ7cwN': '7f5ba5709ad7c6d9e4d71f031d3a2943', 'yDXm7VfJmN': '5f4fa9e694ff8b76b7c1a0418bc5241e', '8TZU7Fn2B': '1f949968fbb13aaf3f462baa42f5682e', 'D53Ne9gN': '9d29d7f41fbf18007a2d01ff7db50c19', '86F83aE': '23d2f4adce858c8a732c1f395c4d2f12', 'A7JUZfx6hX': '2e8f1b640d2b5dab041c2aafec7403a5', 'wV6gDpLjW': '8b2d35487eef6400cc643d6f2baddff2', 'enQxJ3p4': '7e3776600a3c0e4a78e6413e2f61fdd9', 'Pjp7cKPw': '9825c2497e6782c8c8e2f66f0a9b43d1', '95tYZTN9': 'f19b7de0e0c9c6db8fe894e960170eed'}
# Salted Password Hashes: {'9TQ7cwN': 'd6e04f3ac180045cb143dd850b9fd68b', 'yDXm7VfJmN': 'd7821de249c6a27076f67b72410f2973', '8TZU7Fn2B': 'c2e3a198d50b13688e9a5f715500df75', 'D53Ne9gN': '8c798bcf2400df27f3e0121df44c2a4a', '86F83aE': '948da2a06611af169f083c4e5b10e26e', 'A7JUZfx6hX': 'bbce7beeffa0c841f6b77f070d42d3f4', 'wV6gDpLjW': 'b5f2d7a705154c8e36459572b0621a95', 'enQxJ3p4': '23cb7244dbbccfc6617844e00362bc61', 'Pjp7cKPw': '6d4e8166eef4c0dbef636d10ef7af519', '95tYZTN9': '3f7a8e8b44b4e83b03cb0d0f76c7b43b'}

# Password to Authenticate: D53Ne9gN
# Authenticated (without salt): True
# Authenticated (with salt): False
 