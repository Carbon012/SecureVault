from cryptography.fernet import Fernet
from config import Config

cipher_suite = Fernet(Config.ENCRYPTION_KEY)

def encrypt_data(data: str) -> bytes:
    """Encrypts plaintext string to bytes."""
    return cipher_suite.encrypt(data.encode('utf-8'))

def decrypt_data(encrypted_data: bytes) -> str:
    """Decrypts bytes back to plaintext string."""
    return cipher_suite.decrypt(encrypted_data).decode('utf-8')