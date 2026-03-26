from services import *
from files import *

inventory = []
AUTO_PATH = "inventory_auto.csv"

# 🔥 Control de persistencia
data_loaded = False


# ---------------- VALIDADORES ----------------
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


# ---------------- MENÚ ----------------
running = True

while running:

    print("\n--- MENU ---")
    print("1. Add")
    print("2. Show")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Statistics")
    print("7. Sort")
    print("8. Save CSV")
    print("9. Load CSV")
    print("10. Exit")

    option = input("Choose: ")

    # ---------------- AGREGAR ----------------
    if option == "1":
        name = input("Name: ")
        price = get_float("Price: ")
        quantity = get_int("Quantity: ")
        add_product(inventory, name, price, quantity)

    # ---------------- MOSTRAR ----------------
    elif option == "2":
        show_inventory(inventory)

    # ---------------- BUSCAR ----------------
    elif option == "3":
        if not data_loaded:
            print("⚠️ You must load or save a CSV first.")
        else:
            name = input("Search: ")
            print(search_product(inventory, name) or "Not found")

    # ---------------- ACTUALIZAR ----------------
    elif option == "4":
        if not data_loaded:
            print("⚠️ You must load or save a CSV first.")
        else:
            name = input("Update: ")
            price = get_float("New price: ")
            quantity = get_int("New quantity: ")
            update_product(inventory, name, price, quantity)

    # ---------------- ELIMINAR ----------------
    elif option == "5":
        if not data_loaded:
            print("⚠️ You must load or save a CSV first.")
        else:
            name = input("Delete: ")
            delete_product(inventory, name)

    # ---------------- ESTADÍSTICAS ----------------
    elif option == "6":
        if not data_loaded:
            print("⚠️ You must load or save a CSV first.")
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

    # ---------------- ORDENAR ----------------
    elif option == "7":
        if not data_loaded:
            print("⚠️ You must load or save a CSV first.")
        else:
            criteria = input("Sort by (price/quantity): ")
            sort_inventory(inventory, criteria)

    # ---------------- GUARDAR ----------------
    elif option == "8":
        path = input("Path: ")
        save_csv(inventory, path)
        data_loaded = True  # 🔥 activar validación

    # ---------------- CARGAR ----------------
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

            data_loaded = True  # 🔥 activar validación

    # ---------------- SALIR ----------------
    elif option == "10":
        save_csv(inventory, AUTO_PATH)
        print("Auto-saved. Goodbye 👋")
        running = False

    else:
        print("Invalid option.")