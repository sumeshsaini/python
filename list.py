def insert_element(lst, index, element):
    lst.insert(index, element)

def update_element(lst, old_value, new_value):
    if old_value in lst:
        index = lst.index(old_value)
        lst[index] = new_value
    else:
        print("Element not found in the list.")

def delete_element(lst, element):
    if element in lst:
        lst.remove(element)
    else:
        print("Element not found in the list.")

def sort_list(lst, order):
    if order == 'asc':
        lst.sort()
    elif order == 'desc':
        lst.sort(reverse=True)
    else:
        print("Invalid order. Please choose 'asc' or 'desc'.")

def main():
    my_list = []
    n = int(input("Enter the length of the list: "))
    for i in range(n):
        element = input("Enter element {}: ".format(i + 1))
        my_list.append(element)

    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Sort")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter the index to insert: "))
            element = input("Enter the element to insert: ")
            insert_element(my_list, index, element)
            print("List after insertion:", my_list)
        elif choice == 2:
            old_value = input("Enter the element to update: ")
            new_value = input("Enter the new value: ")
            update_element(my_list, old_value, new_value)
            print("List after update:", my_list)
        elif choice == 3:
            element = input("Enter the element to delete: ")
            delete_element(my_list, element)
            print("List after deletion:", my_list)
        elif choice == 4:
            order = input("Enter the order (asc/desc): ")
            sort_list(my_list, order)
            print("List after sorting:", my_list)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()  # Call main function directly
