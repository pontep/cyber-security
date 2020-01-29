from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import hashlib

# Sign
message = open("studentEncrypted.txt","rb").read()
key = RSA.importKey(open('private_key.pem').read())
h = SHA.new(message)
signer = PKCS1_v1_5.new(key)
signature = signer.sign(h)
open("digitalLicense.txt","wb").write(signature)