
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# --------
# Imports
# --------
import base64
from PIL import Image
from io import BytesIO

# --------
# globalvar
# --------
img_data="codebase64"

def main():

    
def fromFile(source,destination):
  with open(destination+"/imageToSave.png", "wb") as handle:
    handle.write(base64.decodebytes(source))

def fromDB(source, destination,idacces,table) :

    
if __name__ == '__main__':
  main()
