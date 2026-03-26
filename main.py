from services import *
from files import *

inventory = []
AUTO_PATH = "inventory_auto.csv"

#Control de persistencia
data_loaded = False

def get_float(msg):
    valid = False
    while not valid:
        try:
            value = float(input(msg))
            if value < 0:
                print("Must be non-negative.")
            else:
                valid = True
        except:
            print("Invalid number.")
    return value


def get_int(msg):
    valid = False
    while not valid:
        try:
            value = int(input(msg))
            if value < 0:
                print("Must be non-negative.")
            else:
                valid = True
        except:
            print("Invalid integer.")
    return value


# Menu
running = True

while running:

    print("\n--- MENU ---\n 1. Add\n 2. Show\n 3. Search\n 4. Update\n 5. Delete\n 6. Statistics\n 7. Sort\n 8. Save CSV\n 9. Load CSV\n 10. Exit")

    option = input("Choose: ")

    if option == "1":
        name = input("Name: ")
        price = get_float("Price: ")
        quantity = get_int("Quantity: ")
        add_product(inventory, name, price, quantity)

    elif option == "2":
        show_inventory(inventory)

    elif option == "3":
        if not data_loaded:
            print("You must load or save a CSV first.")
        else:
            name = input("Search: ")
            print(search_product(inventory, name) or "Not found")

    elif option == "4":
        if not data_loaded:
            print("You must load or save a CSV first.")
        else:
            name = input("Update: ")
            price = get_float("New price: ")
            quantity = get_int("New quantity: ")
            update_product(inventory, name, price, quantity)

    elif option == "5":
        if not data_loaded:
            print("You must load or save a CSV first.")
        else:
            name = input("Delete: ")
            delete_product(inventory, name)

    elif option == "6":
        if not data_loaded:
            print("You must load or save a CSV first.")
        else:
            stats = calculate_statistics(inventory)
            if stats:
                u, v, expensive, stock = stats
                print("Total units:", u)
                print("Total value:", v)
                print("Most expensive:", expensive["name"])
                print("Highest stock:", stock["name"])
            else:
                print("Empty inventory.")

    elif option == "7":
        if not data_loaded:
            print("You must load or save a CSV first.")
        else:
            criteria = input("Sort by (price/quantity): ")
            sort_inventory(inventory, criteria)

    elif option == "8":
        path = input("Path: ")
        save_csv(inventory, path)
        data_loaded = True  #activar validación

    elif option == "9":
        path = input("Path: ")
        new_data = load_csv(path)

        if new_data:
            decision = input("Overwrite? (y/n): ")
            if decision.lower() == "y":
                inventory = new_data
            else:
                for new in new_data:
                    existing = search_product(inventory, new["name"])
                    if existing:
                        existing["quantity"] += new["quantity"]
                        existing["price"] = new["price"]
                    else:
                        inventory.append(new)

            data_loaded = True  #activar validación

    elif option == "10":
        save_csv(inventory, AUTO_PATH)
        print("Auto-saved. Bye")
        running = False

    else:
        print("Invalid option.")