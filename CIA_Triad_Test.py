# This script encrypts and decrypts the contents of User_details.txt
from cryptography.fernet import Fernet
from pathlib import Path
import sys

# Key file
key_file = Path("secret.key")
if not key_file.exists():
	key = Fernet.generate_key()
	key_file.write_bytes(key)
else:
	key = key_file.read_bytes()

cipher = Fernet(key)

input_path = Path("User_details.txt")
if not input_path.exists():
	print(f"Input file not found: {input_path}")
	sys.exit(1)

# Read file bytes
data = input_path.read_bytes()

# Encrypt and write to .enc file
enc_path = input_path.with_name(input_path.name + ".enc")
enc_data = cipher.encrypt(data)
enc_path.write_bytes(enc_data)
print(f"Encrypted: {enc_path}")

# Decrypt and write to a new file
dec_path = input_path.with_name(input_path.stem + "_decrypted" + input_path.suffix)
dec_data = cipher.decrypt(enc_data)
dec_path.write_bytes(dec_data)
print(f"Decrypted: {dec_path}")

# Verify integrity
if data == dec_data:
	print("Verification: SUCCESS — decrypted contents match original")
else:
	print("Verification: FAILURE — decrypted contents differ")