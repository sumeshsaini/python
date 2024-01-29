def new():
    user_tasks = []
    pen = True
    while pen:
        print("Select an option")
        print("Enter 1 to add to your list")
        print("Enter 2 to see your list")
        print("Enter 3 to edit your list")
        print("Enter 4 to delete from your list")
        print("Enter 5 to mark a completed task in your list")
        print("Enter 6 to restart")
        print("Enter 7 to create a new list")

        user_input = int(input("Enter: "))

        if 1 > user_input or user_input > 7:
            print("Invalid input")
        elif user_input == 1:
            task = input("Enter your task: ")
            user_tasks.append({"task": task, "completed": False})
            print("Task added")
        elif user_input == 2:
            if not user_tasks:
                print("You don't have any tasks")
            else:
                print("Your tasks:")
                for index, task_data in enumerate(user_tasks, 1):
                    status = "Completed" if task_data["completed"] else "Pending"
                    print(f"{index}. {task_data['task']} - {status}")
        elif user_input == 3:
            if user_tasks:
                index = int(input("Enter the task number you would like to edit: "))
                if 1 <= index <= len(user_tasks):
                    new_task = input("Enter the new task: ")
                    user_tasks[index - 1]["task"] = new_task
                    print("Task edited")
                else:
                    print("Invalid task number")
            else:
                print("You don't have any tasks")
        elif user_input == 4:
            if user_tasks:
                del_index = int(input("Enter the task number you would like to delete: "))
                if 1 <= del_index <= len(user_tasks):
                    del user_tasks[del_index - 1]
                    print("Task deleted")
                else:
                    print("Invalid task number")
            else:
                print("You don't have any tasks")
        elif user_input == 5:
            if user_tasks:
                comp_task = int(input("Enter the task number you would like to mark as completed: "))
                if 1 <= comp_task <= len(user_tasks):
                    user_tasks[comp_task - 1]["completed"] = True
                    print("Task marked as completed")
                else:
                    print("Invalid task number")
            else:
                print("You don't have any tasks")
        elif user_input == 6:
            user_tasks = []  # Restart by clearing the tasks
            print("Task list cleared")
        elif user_input == 7:
            pen = False
            new()

new()  # Call the new function to start the program