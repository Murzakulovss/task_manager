from task_manager import TaskManager
t = TaskManager()

while True:
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. List Tasks")
    print("6. Exit")

    try:
        choice = int(input("choose a number of option: "))
    except ValueError:
        print("invalid value, enter a number")
        continue

    match choice:
        case 1:
            t.add_task()
        case 2:
            t.delete_task()
        case 3:
            t.update_task()
        case 4:
            t.mark_task_as_done()
        case 5:
            t.get_tasks_list()
        case 6:
            break
        case _:
            print("Invalid option")
