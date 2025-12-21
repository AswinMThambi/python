name=input("Enter your name ")
age=int(input("Enter your age "))

if(age<18):
	print (f"{name} is NOT eligible to vote",name)
else:
	print (f"{name} IS eligilbe to vote",name)
