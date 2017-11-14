from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib

class AESEncDec(object):

    def __init__(self, key): 
        self.key = hashlib.sha256(key.encode()).digest()



    #create initialize vector, cipher_text and encode encrypted message

    def encrypt(self, message):
        message = self._pad(message)
        initial_vector = Random.new().read(AES.block_size)
        cipher_text = AES.new(self.key, AES.MODE_CBC, initial_vector)
        return base64.b64encode(initial_vector + cipher_text.encrypt(message))


    #decode input bytes, create initialize vector, cipher_text and decrypt

    def decrypt(self, encrypted):
        encrypted = base64.b64decode(encrypted)
        initial_vector = encrypted[:AES.block_size]
        cipher_text = AES.new(self.key, AES.MODE_CBC, initial_vector)
        return self._unpad(cipher_text.decrypt(encrypted[AES.block_size:])).decode('utf-8')

    #add to the end of message as many byte as need to get a input message size multiple to AES.block_size
    def _pad(self, string):
        return string + (AES.block_size - len(string) % AES.block_size) * chr(AES.block_size - len(string) % AES.block_size)

    #delete from message unnecessary bytes that was added to counterbalance message size with AES.block_size
    def _unpad(self, string):
        return string[:-ord(string[len(string)-1:])]

