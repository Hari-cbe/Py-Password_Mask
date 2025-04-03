# pip install cryptography
from cryptography.fernet import Fernet
from password_utils import encrypt_password

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key','wb') as file:
        file.write(key)
    print("✅ Secret Key saved.")
    


if __name__ == '__main__':
    # Uncomment it while running for first time 
    generate_key()
    
    # encrypted = encrypt_password('root')
    # print('✅ Password Encrypted.')
    # print(encrypted)