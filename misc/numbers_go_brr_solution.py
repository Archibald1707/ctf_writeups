from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import random

def get_random_number(seed):
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def decrypt(ciphertext_hex, initial_seed):
    ciphertext = bytes.fromhex(ciphertext_hex)
    key = b''
    for i in range(8):
        key += (get_random_number(initial_seed) % (2 ** 16)).to_bytes(2, 'big')
        initial_seed = get_random_number(initial_seed)  # update seed for next iteration
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()
    except ValueError:
        # Decryption failed (possibly due to incorrect key), return None
        return None

def brute_force_decrypt(encrypted_flag_hex):
    for initial_seed in range(10**6 + 1):
        decrypted_flag = decrypt(encrypted_flag_hex, initial_seed)
        if decrypted_flag is not None:
            print("Decrypted flag:", decrypted_flag)
            return True  # Flag decrypted successfully
    print("Failed to decrypt flag.")
    return False  # Flag decryption failed

# Example usage:
encrypted_flag_hex = input("Enter the encrypted flag in hexadecimal: ")
brute_force_decrypt(encrypted_flag_hex)
