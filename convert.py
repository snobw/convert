#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# --------
# Imports
# --------
import base64
import request
import mysql.connector 
from PIL import Image
from io import BytesIO

# --------
# globalvar
# --------
img_data="codebase64"

def main():
#arguments

#boucle d'execution
    
def fromFile(source,destination,name):
  with open(destination+"/"+name, "wb") as handle:
    handle.write(base64.decodebytes(source))

def fromDB(source, destination,idacces,table) :
    cursor.execute("""SELECT id, name, age FROM users WHERE id = %s""", ("5", ))
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

def dataBaseconnection():
    conn = mysql.connector.connect(host="localhost",user="root",password="XXX", database="test1")
    cursor = conn.cursor()

def dataBaseDeconnection():
    conn.close()

#arguments    
if __name__ == '__main__':
  main()
