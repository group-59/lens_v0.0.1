######################################################################################################
#  janeZero3       part of the seedgen file that makes sure no on edits the file with out spescifide #
#                  software.                                                                         #
#  PATREON         MARS JANUS AND JUNO                                                               #
######################################################################################################
import hashlib
## useine stat function of os moduale
import os
import json
from Rseedgen import last_int
## input the file name including the path to that file
## size of the file

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   ## make a hash object
   h = hashlib.sha512()

   ## open file for reading in binary mode
   with open(filename,'rb') as file:

       ## loop till the end of the file
       chunk = 0
       while chunk != b'':
           ## read only 1024 bytes at a time
           chunk = file.read(1012)
           h.update(chunk)

   ## return the hex representation of digest
   return h.hexdigest()

## filehash
file1 = hash_file("seedgen.py")
file2 = hash_file("seedgen-files/seedgenTX.txt")
file3 = hash_file("Rseedgen.py")
file4 = hash_file("filehash.py")
previous_seed = last_int

## file hash should be put in the json as a table or xml
filehashs=(message1, message2, message3, message4, previous_seed)

## filehashs is a tuple
