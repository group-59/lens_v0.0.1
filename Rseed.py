## created by room 109
## reads the seedgenTX.txt file
x=[]
f=open("drive://path/seedgenTX.txt", "r")
for rlist in f:
  A = rlist
  x.append(A)
last_int = x[4]
## check if last_int is the last thing in seedgenTX.txt in there

def devInt(dev_Int):
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
  print("seed_gen interger:\n", devInt(dev_int))
  ##see if the dev_int > grater the devInt(dev_int)
  sub_int = dev_int > devInt(dev_int)
  ## prints out if the sub_int True or False
  if sub_int is False:
    sub_int = dev_int+devInt(dev_int)
    print("dev_int add : False: \n", sub_int)
  if sub_int is True:
    sub_int = dev_int-devInt(dev_int)
    print("sub_int sub: True : \n", sub_int)
## close the seedgenTX.txt
f.close()
