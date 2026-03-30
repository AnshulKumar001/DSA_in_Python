#Type of list
list1=[1,2,3,4]
list2=["anshul","abhi","adhi"]
list3=[1,"ans",10.5,True]
print(list1)
print(list2)
print(list3)


# subtract word
a=list("Anshul")
print(a)

#Access elements
d=[10,20,30,40,50]
print(d[1])
print(d[-1])

#Added Element
c=[]
c.append(10)#Value
c.append(20)
print("After Append Value",c)

c.insert(0,1000)#index
print("After Inster Values",c)

c.extend([11100,00,00])
print("After Extend",c)

c.clear()
print("After clear",c)

#Update
upd=[1, 2, 3, 400]
upd[0]=20000#value
print("After update",upd)


#Delete
upd.remove(400)#value
print("After remove",upd)

upd.pop(1)#index
print("After pop ",upd)

del upd[1]
print("After del",upd)
