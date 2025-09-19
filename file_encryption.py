from cryptography.fernet import Fernet
import os

# --- Key Management Functions ---

def generate_key_and_save(key_filename="secret.key"):
    """
    Generates a Fernet key and saves it to a file.
    Only run this once for a new key.
    """
    key = Fernet.generate_key()
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
    print(f"Key saved to {key_filename}")

def load_key(key_filename="secret.key"):
    """Loads the key from the specified file."""
    if not os.path.exists(key_filename):
        raise FileNotFoundError(f"Key file not found: {key_filename}")
    with open(key_filename, "rb") as key_file:
        return key_file.read()

# --- Encryption/Decryption Functions ---

def encrypt_file(filename, key):
    """Encrypts a file using the provided key."""
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{filename}' encrypted to '{filename}.encrypted'")

def decrypt_file(encrypted_filename, key):
    """Decrypts an encrypted file using the provided key."""
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    original_filename = encrypted_filename.replace(".encrypted", "")
    with open(original_filename + ".decrypted", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"File '{encrypted_filename}' decrypted to '{original_filename}.decrypted'")

# --- Main Script ---
if __name__ == "__main__":
    # Generate a key and save it. Only do this once!
    # Subsequent runs should use the same key.
    key_file = "my_secure.key"
    if not os.path.exists(key_file):
        generate_key_and_save(key_file)
    
    # Load the key from the file
    loaded_key = load_key(key_file)

    # Input the file
    file_name = input("Enter the file: ")

    # Encrypt the file
    encrypt_file(file_name, loaded_key)

    # Decrypt the file
    encrypted_file = input("Enter the file to decrypt: ")
    choice = input("Enter a key?(y/n): " 
    if choice == "y"
        new_key == input("Enter key: ")
	decrypt_file(encrypted_file, new_key)
    elif choice == "n"
	decrypt_file(encrypted_file, loaded_key)
    
