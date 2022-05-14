there are three main files listed

seedgen.py
Rseed.py
filehash.py

seedgen.py --a--> Rseed.py --c--
        \                       \
         ^--b--> filehash.py --c-^--> #? saldedchain

defenitions:
(a) have the out put file example on lines 11 through 15

## seedRX is appended to seedgen.txt for now
f=open("E://lens_v0.0.1-main/seedgen.txt","a")
f.writelines("\n")
f.writelines(seedRX)
f.close()

(b) have the file to be hashed
hashing the seedgen.py and salting with the Rseed.py to put into the hypothetical saldedchain
to lock the file from being edited 
