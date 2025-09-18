import hashlib # used for hashing functions

from Crypto.Cipher import AES # used for encryption
from Crypto.Random import get_random_bytes 

message = input("Enter message: ") # user input message

key = get_random_bytes(16) # generating a 16-byte key
print("Key (save this someplace secure!):", key.hex())

hashed = hashlib.sha256(message.encode()).hexdigest() # creating hash

data = hashed.encode() # converting hashed message to bytes

cipher = AES.new(key, AES.MODE_GCM) # creating cipher
ciphertext, tag = cipher.encrypt_and_digest(data)

nonce = cipher.nonce # used for decryption

print("\n--- Encryption Complete ---") # displaying encryption info
print("Ciphertext:", ciphertext.hex())
print("Tag:", tag.hex())
print("Nonce:", nonce.hex())


cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce) # decrypting cipher
decrypted = cipher_dec.decrypt_and_verify(ciphertext, tag)

print("\n--- Decryption Complete ---") # displayed decrypted (but still hashed) info
print("Decrypted:", decrypted.decode())


