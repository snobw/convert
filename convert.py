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


def main():
#arguments
    fromFile(source,destination,name)
    dataBaseconnection(host,user,password, database)
    fromDB(source, destination,idacces,table)
    dataBaseDeconnection(conn)
    TODO
    
def fromFile(source,destination,name):
    #boucle d'execution
  with open(destination+"/"+name, "wb") as handle:
    handle.write(base64.decodebytes(source))

def fromDB(source, destination,idacces,table) :
    cursor.execute("""SELECT id, name, age FROM t_synk WHERE id = %s""", ("5", ))
    rows = cursor.fetchall()
    #boucle d'execution
    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

def dataBaseconnection(host,user,password, database):
    conn = mysql.connector.connect(host,user,password, database)
    cursor = conn.cursor()
    return cursor

def dataBaseDeconnection(conn):
    conn.close()

#arguments    
if __name__ == '__main__':
  main()
