# importing the tasks module that had already created in this folder

from tasks import TaskManager

# to display the menu for various operations
def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# main function to perform the todo list operation
def todo_list():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            tasks = task_manager.get_tasks()
            for i, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Incomplete"
                print(f"{i + 1}. {task['description']} - {status}")
        
        elif choice == '2':
            description = input("Enter the task description: ")
            task_manager.add_task(description)
        
        elif choice == '3':
            index = int(input("Enter the task number to update: ")) - 1
            completed = input("Mark as completed? (yes/no): ").lower() == 'yes'
            task_manager.update_task(index, completed)
        
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            task_manager.delete_task(index)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice! Please try again.")

todolist = todo_list()
