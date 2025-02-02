def display_menu():
    print("\nTodo List Manager")
    print("===================")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def main():
    todo_list = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo_list.append({'task': task, 'completed': False})
            print(f"Added task: '{task}'")

        elif choice == '2':
            if todo_list:
                print("\nYour Tasks:")
                for index, todo in enumerate(todo_list):
                    status = "✓" if todo['completed'] else "✗"
                    print(f"{index + 1}. [{status}] {todo['task']}")
            else:
                print("Your todo list is empty.")

        elif choice == '3':
            task_number = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_number < len(todo_list):
                removed_task = todo_list.pop(task_number)
                print(f"Deleted task: '{removed_task['task']}'")
            else:
                print("Invalid task number.")

        elif choice == '4':
            task_number = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_number < len(todo_list):
                todo_list[task_number]['completed'] = True
                print(f"Marked task: '{todo_list[task_number]['task']}' as completed.")
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("Exiting the Todo List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
