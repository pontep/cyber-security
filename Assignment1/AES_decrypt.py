import base64
import hashlib
from Crypto.Cipher import AES

def unpad(s): return s[:-ord(s[len(s) - 1:])]

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


# Read encrypted file.
fileUrl = "studentEncrypted.txt"
f = open(fileUrl, 'rb')
s = f.read()
f.close()

# Check if no data.
if s == '':
    print("Error: No data in {}!".format(fileUrl))
    exit()

# Read password.
password = input("Enter encryption password: ")

# Decrypting
decrypted = decrypt(s, password)

if decrypted == b'':
    print("Error: Password is incorrect!")
    exit()

# Write decrypted data.
f = open('studentDecrypted.txt', 'w')
f.write(bytes.decode(decrypted))
f.close()

# Output result
print("\nDecrypted Success!\n{}\n".format(bytes.decode(decrypted)))