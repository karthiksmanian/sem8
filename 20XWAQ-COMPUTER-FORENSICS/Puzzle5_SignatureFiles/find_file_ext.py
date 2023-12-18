# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import magic

ext = magic.from_file("Z:/20XWAQ-COMPUTER-FORENSICS/Puzzle5_SignatureFiles/File01")

file_extensions = []

files = ["File01","File02","File03","File04","File05","File06","File07"]

for file in files:
    ext = magic.from_file("Z:/20XWAQ-COMPUTER-FORENSICS/Puzzle5_SignatureFiles/"+file, mime=True)
    file_extensions.append(ext)
    

for file_extension in file_extensions:
    print(file_extension)
    
print("EnD.")