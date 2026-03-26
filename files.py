import csv


def save_csv(inventory, path):
    if len(inventory) == 0:
        print("No data to save.")
        return

    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["id", "name", "price", "quantity"])

            for p in inventory:
                writer.writerow([p["id"], p["name"], p["price"], p["quantity"]])

        print(f"Saved in: {path}")

    except Exception as e:
        print("Error saving file:", e)


def load_csv(path):
    inventory = []
    errors = 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            if header != ["id", "name", "price", "quantity"]:
                print("Invalid file format.")
                return []

            for row in reader:
                if len(row) != 4:
                    errors += 1
                    continue

                try:
                    product = {
                        "id": int(row[0]),
                        "name": row[1],
                        "price": float(row[2]),
                        "quantity": int(row[3])
                    }

                    if product["price"] < 0 or product["quantity"] < 0:
                        errors += 1
                    else:
                        inventory.append(product)

                except:
                    errors += 1

        if errors > 0:
            print(f"{errors} invalid rows skipped.")

        return inventory

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error loading file:", e)

    return []