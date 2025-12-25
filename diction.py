student={ "name" : "aswin",
"age" : 21,
"course" : "Btech_cs",
"is_finalyear" : True
}

print ("The name of the student is \n",student["name"])
print ("The age of the student is \n",student["age"])

print ("\nAll the details of the student")
for key,value in student.items():
	print (key,":",value)
#updating the values

student["age"] = 22
student["college"] = "cusat"

print ("Updated values: \n")
for key,value in student.items():
	print (key,":",value)

