import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random


BLOCK_SIZE = 16

def pad(s): return s + (BLOCK_SIZE - len(s) %
                        BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


# Read text file.
f = open('student.txt', 'r')
s = f.read()
f.close()
# # Read another file.
data = open('4918.jpg','rb').read()
digest = hashlib.sha256(data).hexdigest()

# Check file is empty?
if s == '':
    print("Error: Text file is empty. Please fill something in {}!".format(fileUrl))
    exit()

# Read password for AES encryption.
password = input("Enter encryption password: ")

# Encrypting.
encrypted = encrypt(s, password)
f = open('studentEncrypted.txt', 'wb')
f.write(encrypted)
f.close()

encrypted = encrypt(data, password)
open('4918.aes','wb').write(encrypted)

# Output
print("Encrypted success!")