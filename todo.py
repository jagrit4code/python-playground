todos = []
while True:
    print("1. add task")
    print("2. view tasks")
    print("3. quit")
    choice = input("enter your choice ")
    if choice == "1":
        task = input("enter a task ")
        todos.append(task)
    elif choice == "2":
        print(todos)
    elif choice == "3":
        break

    
    