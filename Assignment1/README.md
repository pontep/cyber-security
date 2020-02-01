# Cyber Security  
## Assignment 1  
### Member  
- B6003296 PUMMARIN PHIAWSOONGNERN @pummarin  
- B6000783 PONTEP THAWEESUP @pontep  
  
### How To Run  
#### Generating private and public key  
1. run gen_key.py  

#### AES Encrypting text file + Create Digital License.  
1. run AES_encrypt.py : Encrypting 'student.txt' to 'studentEncrypted.txt' with AES 128 bit.  
2. run sign.py : Sign encrypted student by private key.  
  
#### Verify Digital License + AES Decrypting text file.
1. run verify.py : verify by public key.  
2. run AES_decrypt.py : Decrypting 'studentEncrypted.txt' to 'studentDecrypted.txt'.  
 
#### AES Encrypting other file.  
1. run encode_otherfile.py : Encrypting 'pic.jpg' to 'pic.jpg.aes' with AES 128 bit.  

#### AES Decrypting other file.  
1. run decode_otherfile.py : Decrypting 'pic.jpg.aes' to 'pic2.jpg'.  

### Doc | Reference  
- https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto  

