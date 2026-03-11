todos = []
while True:
    print("1.add tasks")
    print("2.view tasks")
    print("3.exit")
    choice = input("enter your choice")
    if choice == "1":
        task = input("enter a task")
        todos.append(task)
    elif choice == "2":
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        break
