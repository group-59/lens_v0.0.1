######################################################################################################
#  janeZero3       part of the seedgen file that makes sure no on edits the file with out spescifide #
#                  software.                                                                         #
#  PATREON         MARS JANUS AND JUNO                                                               #
######################################################################################################
import hashlib
# useine stat function of os moduale
import os

# input the file name including the path to that file
# size of the file
file_size = os.stat(input("filename: "))

h= hashlib.sha256()
h.update(str(file_size).encode('utf-8'))
h.hexdigest()

print("format the file that will be hashed including path to the file")
print("file name that is going to get hashed: \n", file_size)
print("size of the file : \n",file_size.st_size, "bytes")
print("hash of the file: \n", h.hexdigest())
'''
filename: seedgen.py
format the file that will be hashed including path to the file
file name that is going to get hashed:
 os.stat_result(st_mode=33206, st_ino=11204034656, st_dev=2988945333, st_nlink=1, st_uid=0, st_gid=0, st_size=3269, st_atime=1652486274, st_mtime=1652486274, st_ctime=1652481291)
size of the file :
 3269 bytes
hash of the file:
 bb656a581206082b17d5949ddb9f00160a710b151a2ae977bddedbd8a6413f87
'''