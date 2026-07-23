
tasks = []


def add_task():
    task_id = input("enter task id: ").strip()
    task_title = input("enter task title: ")
    priority = input("enter task priority: ")
    date = input("enter task date (e.g. DD-MM-YYYY) :").strip()

    task = {
        "id": task_id,
        "title": task_title,
        "priority": priority,
        "date": date,
        "completed": False
    }

    tasks.append(task)

    print("Add task succesfully! ")


def view_tasks():
    if not tasks:
        print("Task not found")
        return

    for task in tasks:
        print("*" * 25)
        print("       TODO LIST")
        print("*" * 25)

        print(f"Id         :{task['id']}")
        print(f"Title      :{task['title']}")
        print(f"Priority   :{task['priority']}")
        print(f"date       :{task['date']}")
        status = "completed" if task['completed'] else "pending"
        print(f"status     :{status}")

        # if task['completed']:
        #     print("Status    : Completed")   # uporer ta etar sort tarm

        # else:
        #     print("Status    : Pending")


def search_task():
    search_id = input("Enter task is for search: ")
    for task in tasks:
        if search_id == task['id']:
            print("*" * 25)
            print("       TODO LIST")
            print("*" * 25)

            print(f"Id         :{task['id']}")
            print(f"Title      :{task['title']}")
            print(f"Priority   :{task['priority']}")
            print(f"date       :{task['date']}")
            status = "Completed" if task['completed'] else "Pending"
            print(f"status     :{status}")

            return

    print("\ntask not found!")


def update_task():
    task_id = input("enter task id for update task: ")
    for task in tasks:
        if task_id == task['id']:
            new_title = input("enter new task title: ")
            new_priority = input("enter new task priority: ")
            new_date = input("enter new task date : ")
            # status = input("enter new status :")

            task['title'] = new_title
            task['priority'] = new_priority
            task['date'] = new_date
            print("\nTask update succesfully! ")

            return

    print("Task id not found! ")


def delete_task():
    delete_id = input("enter task id for delete task: ")
    for task in tasks:
        if delete_id == task['id']:
            tasks.remove(task)
            print("\nDelete task succesfully.!")
            return

    print("\nTask nou found")


def mark_task_completed():
    mark_task_id = input('enter task id for mark_completed : ')
    for task in tasks:
        if mark_task_id == task['id']:
            task["completed"] = True
            print("\nmark completed task sccesfully")
            return

    print("\nTask id not found")


def pending_task():
    if not tasks:
        print("\nTask list is empty")
        return
    for task in tasks:
        if not task['completed']:

            print(f"Id         :{task['id']}")
            print(f"Title      :{task['title']}")
            print(f"Priority   :{task['priority']}")
            print(f"date       :{task['date']}")
            status = "Completed" if task['completed'] else "Pending"
            print(f"status     :{status}")


def completed_task():

    if not tasks:
        print("\nTask file empty")
        return

    for task in tasks:
        if task['completed']:
            
                 print(f"Id         :{task['id']}")
                 print(f"Title      :{task['title']}")
                 print(f"Priority   :{task['priority']}")
                 print(f"date       :{task['date']}")
                 status = "Completed" if task['completed'] else "Pending"
                 print(f"status     :{status}")


def export_csv():
    pass
