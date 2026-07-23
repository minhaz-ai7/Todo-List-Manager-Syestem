import json



def load_tasks():
    try:
        with open("todo_list_manager/tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks

    except FileNotFoundError:
        return []
    
    
def save_tasks(tasks):
        with open ("todo_list_manager/tasks.json" , "w") as file:
            json.dump(tasks , file , indent=4)
            
    
    
    

