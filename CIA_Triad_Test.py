# This is a simple test of the CIA triad using the Fernet symmetric encryption scheme from the cryptography library.
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

text = b"Super Secret Message"
cipher_text = cipher_suite.encrypt(text)
print({f"Encrypted: {cipher_text}"})

# Decrypt the cipher text
decrypted_text = cipher_suite.decrypt(cipher_text)
print({f"Decrypted: {decrypted_text}"})