student = { "name" : "achu",
"age" : 21,
"course" : "Btech",
"is_finalyear" : True,
}

print ("The name of student: \n",student["name"])
print ("The age of the student: \n",student["age"])

print ("All the student details\n")
for key,value in student.items():
	print (key, ":",value)

student["age"] = 22
student["college"] = "cusat"

print ("\nUpdated student details")

for key,value in student.items():
	print (key,":",value)




