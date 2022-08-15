import contextlib
import shutil
import os
from cryptography.fernet import Fernet
import uuid
name = input("Enter the name of the computer: ")

shutil.copytree("./Majumder Clone Bot", f"./New/{name}")

with contextlib.suppress(Exception):
    shutil.rmtree(f"./New/{name}/output")

KEY = Fernet.generate_key()


 
fernet = Fernet("QtL_rD8NiJvtEgknC8KMbS0l75sowlINBV-V3q3mwqA=".encode())

 
def encrypt(file):
    try: 
        encryptedMyFileData = fernet.encrypt(name.encode())
        with open(file, "wb") as myFile:
            myFile.write(encryptedMyFileData)
    except Exception as e:
        return

fileName = f"./New/{name}/f3220fcc-62ec-4744-bd0e-52aacff1539d.txt"
with open(fileName, "wb") as f:
    pass

encrypt(fileName)