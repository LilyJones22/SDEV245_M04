import hashlib # used for hashing functions

from Crypto.Cipher import AES # used for encryption
from Crypto.Random import get_random_bytes 

print("-" * 19)
print("-- Opening Email --")
print("-" * 19)

message = input("What would you like to send?\n") # user input message

key = get_random_bytes(16) # generating a 16-byte key

print("   --[KEY]--")
print(" STORE SECURILY")
print(key.hex()) # displaying key

hashed = hashlib.sha256(message.encode()).hexdigest() # creating hash

data = hashed.encode() # converting hashed message to bytes

cipher = AES.new(key, AES.MODE_GCM) # creating cipher
ciphertext, tag = cipher.encrypt_and_digest(data)

nonce = cipher.nonce # used for decryption


print("\n-- MESSAGE SENT --")
print("-" * 18)
print("Ciphertext:", ciphertext.hex())
print("Tag:", tag.hex())
print("Nonce:", nonce.hex())

print("")
print("-" * 9)
print(" Goodbye ")
print("-" * 9)

print("\n" * 3)

print("-" * 19)
print("-- Opening Email --")
print("-" * 19)

print(" [NEW MESSAGE RECIEVED] ")
print("Please Input Key to Decrypt")

text = input() # Recipent has to input key

while bytes.fromhex(text) != key: # verifying key matches message
    print("Not Correct. Please Try Again")
    text = input()

cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce) # decrypting cipher
decrypted = cipher_dec.decrypt_and_verify(ciphertext, tag)

print("\nIdentity Verified")
print("MESSAGE")
print("-------\n")
print(decrypted.decode())