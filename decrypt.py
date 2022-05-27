#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file in ["encrypt.py", "key", "decrypt.py"]:
        continue
    if os.path.isfile(file):
        files.append(file)

with open("key", "rb") as fp:
    my_key = fp.read()

for file in files:
    with open(file, "rb") as fp:
        contents = fp.read()
    decrypted_contents = Fernet(my_key).decrypt(contents)
    with open(file, "wb") as fp:
        fp.write(decrypted_contents)
