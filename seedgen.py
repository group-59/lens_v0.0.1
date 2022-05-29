'''
###########################################################################################
please read the READ.ME
###########################################################################################
                        credits for seedgen.py
ROOM 109  owns the right ti this seedgen.py aka group-59
ld98      for putting every thing together and making it coherent
group-95  for letting ld98 use their servers to test
###########################################################################################
                          aditional credits
greenapple-alicia-nurale-network      using the expertise in the networking
                                      and cloud computing
###########################################################################################
'''

#moduals that come with python v3.9
import random

# random number genarator
#random.seed(int)
x = []    #list

for i in range(6):
  A =random.randint(10,20)
  x.append(A)
#print('x int : \n', x)
a = x[0]
b = x[1]
c = x[2]
d = x[3]
e = x[4]
f = x[5]
  
ranZero = (a, b, c, d, e, f)
ranOne = a+b+c+d+e+f
ranTwo = a+1+b+2+c+3+d+4+e+5+f+6
ranThree = a+1+3+b+2+5+c+3+7+d+4+11+e+5+13+f+6+17


## seed that are created♪
seedZero = ranZero
seedOne = ranOne*16*155**512
seedTwo = ranTwo*16*155**512
seedThr = ranThree*16*155**512

## leave ranZero out. its a table
abcdef_multi = ranOne+ranTwo+ranThree
#print('ran123:',abcdef_multi)
## leng of between 1000 1500
seed_gen = ranOne+seedOne+ranTwo+seedTwo+ranThree+seedThr*16+abcdef_multi**512

## seedInt is making sure that seed is a string not an interger
## for writting to seedgen.txt

seed_int = seed_gen
#print("seed_gen intger :\n", seed_int)
seed_sum = seed_int

## seed dictionary
seed = {
  "seedZero": seedZero,
  "seedOne" : seedOne,
  "seedTwo" : seedTwo,
  "seedthr" : seedThr,
  "ran123"  : abcdef_multi,
  "seed_gen": seed_gen,
}
#for x,y in seed.items():
#  print(x,y)

seedRX = "{}".format(seed_sum)
newseed = seedRX
## seedRX is writen to seedgen-file/seedgen.txt

f=open("G://lens_v0.0.1/seedgen-files/seedgenTX.txt","w")
f.writelines(seedRX)
f.close()

print('done generating seed :')