from task import (add_task ,
                  view_tasks ,
                  search_task ,
                  update_task ,
                  delete_task ,
                  mark_task_completed,
                  pending_task,
                  completed_task)

def show_menu():

    print("=" * 35)
    print("        TO-DO LIST MANAGER")
    print("=" * 35)

    print("\n1. Add task")
    print('2. view task')
    print("3. search task")
    print("4. update task")
    print("5. delete task")
    print("6. mark task as completed")
    print("7. view pending task")
    print("8. view completed task")
    print("9. export csv")
    print("10. exit")


def main():
    while True:

        show_menu()
        choice = input("Enter your choice : ")

        if choice == "1":
            add_task()
            
        elif choice == "2":
           view_tasks()
            
        elif choice == "3":
           search_task()
            
        elif choice == "4":
           update_task()
            
        elif choice == "5":
            delete_task()
            
        elif choice == "6":
            mark_task_completed()
            
        elif choice == "7":
           pending_task()
            
        elif choice == "8":
            completed_task()
            
        elif choice == "9":
            print("\nexport csv succesfully")
            
        elif choice == "10":
            print("\nThank you for using to-do list manager system 😊")
            break
        
        else:
            print("Invalid choice ..! please try again ")


if __name__ == "__main__":
    main()