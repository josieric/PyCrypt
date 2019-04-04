
from setuptools import setup

setup(name='PyCrypt',
      version='0.1',
      description='Crypt/Uncrypt with AES in python3',
      author='ToRicSoft Circus',
      author_email='eric.josien@free.fr',
      url='https://github.com/josieric/PyCrypt',
      license='MIT',
      packages=['PyCrypt'],
      install_requires=[
          'Crypto','base64','hashlib'
      ],
      zip_safe=False)

