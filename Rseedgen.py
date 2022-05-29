## created by room 109

from seedgen import newseed

## reads the seedgenTX.txt file
rlistX=[]
f=open("G://lens_v0.0.1/seedgen-files/seedgenTX.txt", "r")
for rlist in f:
  A = rlist
  rlistX.append(A)
  last_int = rlistX.pop(0)
##print("new seed",last_int)

current_seed = newseed == last_int

if current_seed  is False:
  print("last_int not newseed")
  f=open("seedgen.trs", "w")
  f.writelines(bin(int(last_int)))
  f.close()
  print("your seed gen file is misconfigurd")
if current_seed is True:
  pass

  ## check if last_int is the last thing in seedgen-files/seedgenTX.txt in there

  def devInt(dev_int):
    ## converting seed_int to a String
    sss = str(dev_int)
    ## reversing the string
    sss = list(sss)
    sss.reverse()
    sss = ''.join(sss)
    ## converting dev_int string to intger
    dev_int = int(sss)
    ## returning intger
    return dev_int
  ## Driver code
  if __name__ == "__main__":
    dev_int = int(last_int)
    #print("seed_gen interger:\n", devInt(dev_int))

    ## dev_int us a
    ## see if the dev_int > grater the devInt(dev_int)
    sub_int = dev_int > devInt(dev_int)
  #  sub_int = sub_int_pos
  #  sub_int = sub_int_nev

    #print(sub_int)
    ## prints out if the sub_int True or False
    if sub_int is False:
      sub_int_pos = dev_int+devInt(dev_int)
      print("dev_int small and is added: False: \n", sub_int_pos)
    if sub_int is True:
      sub_int_nev = dev_int-devInt(dev_int)
      print("sub_int big and is sub: True : \n", sub_int_nev)
  ## close the seedgenTX.txt
f.close()