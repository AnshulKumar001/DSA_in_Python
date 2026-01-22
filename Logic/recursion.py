#Recursion
#count=0
#def func():
#    global count
#    if count==4:
#        return
#    print("Anshul")
#    count+=1
#    func()
#func()       
   



##count=0
#def fun():
#    global count
#    if count==4:
#        return 
#    print("Anshul Kumar") 
#    count+=1
#    fun()
#fun()

def fun(x,n):
    if n==0:
        return
    print(x)
    fun(x,n-1)
fun("Ans",4)    


