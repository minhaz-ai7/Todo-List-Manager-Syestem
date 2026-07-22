
tasks = []

def add_task():
    task_id = input("enter task id: ").strip()
    task_title = input("enter task title: ")
    priority = input("enter task priority: ")
    date = input("enter task date (e.g. DD-MM-YYYY) :").strip()
    
    
    task = {
        "id" : task_id,
        "title" : task_title,
        "priority" : priority ,
        "date" : date,
        "completed" : False
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
    pass


def update_task():
    pass


def delete_task():
    pass


def mark_completed_task():
    pass


def pending_task():
    pass



def completed_task():
    pass



def export_csv():
    pass