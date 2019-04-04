#! /usr/bin/env python3

from PyCrypt import AESCipher

e = AESCipher('Secret')
print(e.encrypt('coucou'))
print(e.encrypt('coucou'))
print(e.decrypt(e.encrypt('coucou')))

e = AESCipher('AutreSecret')
print(e.encrypt('coucou'))
print(e.encrypt('coucou'))
print(e.decrypt(e.encrypt('coucou')))

