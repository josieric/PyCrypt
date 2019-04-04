# PyCrypt

* install
git clone https://github.com/josieric/PyCrypt.git  
cd PyCrypt/PyCrypt  
python setup.py PyCrypt  
pip install sdist/PyCrypt-0.1.tar.gz  

* import module in python & use it  
from PyCrypt import AESCipher  

e = AESCipher('Secret')  
print(e.encrypt('coucou'))  
print(e.encrypt('coucou'))  
print(e.decrypt(e.encrypt('coucou')))  

e = AESCipher('AutreSecret')  
print(e.encrypt('coucou'))  
print(e.encrypt('coucou'))  
print(e.decrypt(e.encrypt('coucou')))  

