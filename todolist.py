def new () :
    #import time
    user_task = []
    pen = True
    while pen :
        #time = time.strftime("%I:%M:%S")
        #print(time)
        print("\nSelect an option\n")
        print("Enter 1 to add to your list : ")
        print("Enter 2 to see to your list : ")
        print("Enter 3 to edit to your list : ")
        print("Enter 4 to delete from your list : ")
        print("Enter 5 to mark a completed task to your list : ")
        print("Enter 6 to restart : ")
        print("Enter 7 to create a new list : ")
        user_input = int(input("Enter : "))
        if 1> user_input or user_input>7:
            print("Invalid input")
        elif user_input == 1:
            check = True
            while check :
                k = input("Enter your task : ")
                user_task.append ({"task" : k,"Completed" : False})
                print("Task added")
                if (input("Do you still want to add to your list yes or no : ")) == 'no':
                    check = False
        elif user_input == 2 :
            if not user_task:
                print("You dont have any tasks")
            else :
                print("You have following tasks")
                for number, k_d in enumerate (user_task,1):
                    status = "Completed" if k_d ["Completed"] else"Pending"
                    print(f"{number} : {k_d['task']} : {status}")
        elif user_input == 3:
            if user_task:
                index = int(input("Enter the task number you would like to edit : "))
                if 1 <= index <= len(user_task):
                    new_task = input("Enter the new task: ")
                    user_task[index - 1]["task"] = new_task
            print("Task Edited")
        elif user_input == 4:
            del_index = int(input("Enter the task number which you would like to delete :"))
            del user_task[del_index-1]
            print("Your task is updated.")
        elif user_input == 5:
            comp_task = int(input("Enter the task number you would like to mark as completed : "))
            user_task[comp_task-1]["Completed"] = True
            print("Task mark as completed")
        elif user_input == 6:
            user_task = []
            print("Task list is cleared")
        elif user_input == 7:
            pen = False
            new()
new()