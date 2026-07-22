from task import add_task , view_tasks

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
            print("search task succesfully")
            
        elif choice == "4":
            print("update task succesfully")
            
        elif choice == "5":
            print("delete task succesfully")
            
        elif choice == "6":
            print("mark task as completed suffesfully")
            
        elif choice == "7":
            print("view pending task succesfully")
            
        elif choice == "8":
            print("view completed task succesfully")
            
        elif choice == "9":
            print("\nexport csv succesfully")
            
        elif choice == "10":
            print("\nThank you for using to-do list manager system 😊")
            break
        
        else:
            print("Invalid choice ..! please try again ")


if __name__ == "__main__":
    main()