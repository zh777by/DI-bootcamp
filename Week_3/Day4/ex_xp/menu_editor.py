from menu_manager import MenuManager  
from menu_item import MenuItem  

def show_user_menu():
    print("*********** MENU EDITOR ***********")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("Q - Quit")
    print("************************************")

def view_item():
    item_name = input("Enter the name of the item to view: ")
    menu_item = MenuManager.get_by_name(item_name)

    if menu_item:
        print("\nItem found:")
        menu_item.display()
    else:
        print(f"\nItem '{item_name}' not found.")

def add_item():
    name = input("Enter the name of the new item: ")
    price = float(input("Enter the price of the new item: "))

    new_item = MenuItem(name=name, price=price)
    new_item.save()

    print(f"\nItem '{name}' added successfully.")

def delete_item():
    item_name = input("Enter the name of the item to delete: ")
    menu_item = MenuManager.get_by_name(item_name)

    if menu_item:
        menu_item.delete()
        print(f"\nItem '{item_name}' deleted successfully.")
    else:
        print(f"\nItem '{item_name}' not found.")

def update_item():
    item_name = input("Enter the name of the item to update: ")
    menu_item = MenuManager.get_by_name(item_name)

    if menu_item:
        new_name = input("Enter the new name (press Enter to keep the current name): ")
        new_price = float(input("Enter the new price (press Enter to keep the current price): "))

        menu_item.update(new_name=new_name if new_name else None, new_price=new_price if new_price else None)
        print(f"\nItem '{item_name}' updated successfully.")
    else:
        print(f"\nItem '{item_name}' not found.")

def show_menu():
    all_items = MenuManager.all_items()

    if all_items:
        print("\n*********** CURRENT MENU ***********")
        for item in all_items:
            print(f"Item ID: {item['item_id']}, Name: {item['item_name']}, Price: {item['item_price']}")
        print("************************************")
    else:
        print("\nNo items in the menu.")


def add_item_to_menu():
    name = input("Enter the name of the new item: ")
    price = float(input("Enter the price of the new item: "))

    new_item = MenuItem(name=name, price=price)
    new_item.save()

    print(f"\nItem '{name}' added to the menu successfully.")


def remove_item_from_menu():
    item_name = input("Enter the name of the item to remove: ")
    menu_item = MenuItem(name=item_name)  

    try:
        menu_item.delete()
        print(f"\nItem '{item_name}' removed from the menu successfully.")
    except Exception as e:
        print(f"\nError: {e}. Unable to remove item '{item_name}' from the menu.")


def update_item_from_menu():
    item_name = input("Enter the name of the item to update: ")
    item_price = float(input("Enter the price of the item to update: "))
    new_name = input("Enter the new name (press Enter to keep the current name): ")
    new_price = float(input("Enter the new price (press Enter to keep the current price): "))

    menu_item = MenuItem(name=item_name, price=item_price)  

    try:
        menu_item.update(new_name=new_name if new_name else None, new_price=new_price if new_price else None)
        print(f"\nItem '{item_name}' updated successfully.")
    except Exception as e:
        print(f"\nError: {e}. Unable to update item '{item_name}'.")


def show_restaurant_menu():
    all_items = MenuManager.all_items()

    if all_items:
        print("\n*********** RESTAURANT MENU ***********")
        for item in all_items:
            print(f"Item ID: {item['item_id']}, Name: {item['item_name']}, Price: {item['item_price']}")
        print("**************************************")
    else:
        print("\nNo items in the restaurant menu.")



if __name__ == "__main__":
    while True:
        show_user_menu()

        user_choice = input("Enter your choice: ").upper()

        if user_choice == "V":
            view_item()
        elif user_choice == "A":
            add_item_to_menu()
        elif user_choice == "D":
            remove_item_from_menu()
        elif user_choice == "U":
            update_item_from_menu()
        elif user_choice == "S":
            show_menu()
        elif user_choice == "R":
            show_restaurant_menu()
        elif user_choice == "Q":
            print("Exiting the menu editor. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")






