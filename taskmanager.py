tasks = []

def add_task(title) :
	task = {"title" : title,"done" : False}
	tasks.append(task)
	print ("Task has been added successfully!\n")

def view_tasks() :
	if not tasks :
		print ("There are no tasks..\n")
		return

	print ("Here's the list of tasks-\n")
	for index,task in enumerate(tasks) :
		status = "Done" if task["done"] else "Pending"
		print (f"{index + 1}.{task['title']}-{status}\n\n")

def mark_as_done(task_number) :
	if task_number < 1 or task_number > len(tasks) :
		print ("Invalid Input..\n")
		return

	tasks[task_number - 1]["done"] = True
	print ("Task marked as done!\n")

while True :
	print ("\nWelcome to the Task_Manager\n\nChoose your action : ")
	print ()
	print ("1)Add Task\n")
	print ("2)View Tasks\n")
	print ("3)Mark Tasks Done\n")
	print ("4)Exit\n")

	choice = input()
	if choice == "1" :
		title = input ("Enter the task-\n")
		add_task(title)

	elif choice == "2" :
		view_tasks()

	elif choice == "3" :
		task_number = int(input("Task Number Please -\n"))
		mark_as_done(task_number)

	elif choice == "4" :
		print ("Exiting...\n")
		break
	else:
		print ("Invalid Input\n")
