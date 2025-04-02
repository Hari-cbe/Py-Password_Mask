from cryptography.fernet import Fernet

class FakeStar(str):
    def __str__(self):
        return '*****'
    def __repr__(self):
        return '*****'

def load_key():
    return open('secret.key','rb').read()


def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(password).decode()
    return FakeStar(decrypted)

def get_password():
    encrypted_password ="gAAAAABn7Wbjn8qoD8sjeQ1VqP1waLrMjI45czW-42Zu__1iFe6n2y1exwmKsCR23mC8671waKBVkV3Ga_Z5Iqauw3PtI6YM8g=="
    return decrypt_password(encrypted_password)