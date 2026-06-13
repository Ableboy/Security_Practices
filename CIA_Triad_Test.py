# This is a simple test of the CIA triad using the Fernet symmetric encryption scheme from the cryptography library.
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

text = "Super Secret Message from the CIA Triad Test"
cipher_text = cipher_suite.encrypt(text.encode())
print({f"Encrypted: {cipher_text}"})

# Decrypt the cipher text
decrypted_text = cipher_suite.decrypt(cipher_text)
print({f"Decrypted: {decrypted_text}"})