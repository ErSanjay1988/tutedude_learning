#Dictionaries
dict_Student={
    "Sanjay":20,
    "Alice":85,
    "Steave":100
}
name=input("Enter the Student's name :")
if name in dict_Student.keys():
    print(name,"'s Marks:",dict_Student[name])
else:
    print("Student not found.")    