# import array as arr
from array import *
res=0
val=array('i',[1,2,0,4,5,6])
for i in range (0,len(val)):
    print(val[i],end=' ')
val.insert(0,0)
print('/n')    

rev=val.reverse() 
rev=array(val.typecode, (x*10 for x in val))
rev.pop(6)
for i in range (0,len(rev)):
    print(rev[i],end=' ')





#for x in val :
#    print(x,end=" ")
