tasks = []

def add_task(title) :
	task = {"title" : title,
		"done" : False}
	tasks.append(task)
	print ("Task added successfully!")

def view_tasks() : 
	if not tasks : 
		print ("There is no tasks...")
		return

	for index, task in enumerate(tasks) :
		status = "Done" if task["done"] else "Pending"
		print (f"{index + 1}.{task["title"]}-{status}")

def mark_done(task_number) :
	if task_number < 1 or task_number > len(tasks) : 
		print ("Not valid")
		return

	tasks[task_number-1]["done"] = True
	print ("Task marked as done!")

while True :
	print ("1) Add Tasks\n")
	print ("2)View Tasks\n")
	print ("3)Mark Tasks As Done\n")
	print ("4)Exit\n")

	choice = input("Enter your selection..\n")

	if choice == "1" :
		title = input("Task Title Please:\n")
		add_task(title)

	elif choice == "2" :
		view_tasks()
	elif choice == "3" :
		task_number = int(input("Give the completed task nuumber\n"))
		mark_done(task_number)
	elif choice == "4" :
		print ("Exiting...\n")
		break
	else :
		print ("Invalid Input!") 
