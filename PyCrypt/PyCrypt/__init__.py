#! /usr/bin/env python3
# coding: utf-8

from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib

pad = lambda s, BS: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s, BS : s[:-ord(s[len(s)-1:])]

class AESCipher:
    def __init__( self, key ):
        self.BS=16
        self.key = hashlib.md5(key.encode()).hexdigest()[:self.BS]
    def encrypt( self, raw ):
        raw = pad(raw,self.BS)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode()
    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:self.BS]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[self.BS:] ), self.BS).decode()


