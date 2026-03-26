# Generate unique ID
def generate_id(inventory):
    if len(inventory) == 0:
        return 1
    return inventory[-1]["id"] + 1


def add_product(inventory, name, price, quantity):
    product = {
        "id": generate_id(inventory),
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)
    print(f"Product added with ID: {product['id']}")


def show_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for p in inventory:
            print(f"ID: {p['id']} | {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")


def search_product(inventory, name):
    for p in inventory:
        if p["name"].lower() == name.lower():
            return p
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    product = search_product(inventory, name)

    if product:
        if new_price is not None:
            product["price"] = new_price
        if new_quantity is not None:
            product["quantity"] = new_quantity
        print("Product updated.")
    else:
        print("Product not found.")


def delete_product(inventory, name):
    product = search_product(inventory, name)

    if product:
        inventory.remove(product)
        print("Product deleted.")
    else:
        print("Product not found.")


def sort_inventory(inventory, criteria):
    if criteria == "price":
        inventory.sort(key=lambda p: p["price"])
    elif criteria == "quantity":
        inventory.sort(key=lambda p: p["quantity"])

    print(f"Inventory sorted by {criteria}.")


def calculate_statistics(inventory):
    if len(inventory) == 0:
        return None

    total_units = 0
    total_value = 0

    subtotal = lambda p: p["price"] * p["quantity"]

    for p in inventory:
        total_units += p["quantity"]
        total_value += subtotal(p)

    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock = max(inventory, key=lambda p: p["quantity"])

    return (total_units, total_value, most_expensive, highest_stock)