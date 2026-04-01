student={}
student={"Name":"Anshul Kumar","Age":20,"Course":"Machine Learning"}
print(student)
print(student["Age"])#key

#Add
student["City"]="Muzaffarngar"
print(student)

#Update
student["Age"]=21
print(student)

#Delete
del student["Course"]
print(student)