import csv

orders = {}
products = {}


def export_orders_to_csv():
    filename = "orders.csv"

    file = open(filename, mode="w", newline="")

    writer = csv.writer(file)

    writer.writerow(["Customer Name", "Product Name", "Quantity", "Total Amount"])

    for cname, orders_list in orders.items():
        for order in orders_list:
            writer.writerow([
                cname,
                order["product"],
                order["quantity"],
                order["total"]
            ])

    file.close()

    print("Orders exported successfully")


def add_products():
    pid = input("Enter product Id: ")

    if pid in products:
        print("Product already exists")

    else:
        name = input("Enter the product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter the quantity: "))

        products[pid] = {
            "name": name,
            "price": price,
            "stock": stock
        }

        print("Product added successfully")


def view_products():

    if not products:
        print("No product available")

    else:
        print("\nAvailable Products")

        for pid, details in products.items():
            print(
                f"Id:{pid}, Name:{details['name']}, "
                f"Price:{details['price']}, Stock:{details['stock']}"
            )


def place_order():

    pid = input("Enter productId to buy: ")

    if pid in products:

        quantity = int(input("Enter quantity: "))

        if 0 < quantity <= products[pid]["stock"]:

            cname = input("Enter your name: ")

            total = quantity * products[pid]["price"]

            products[pid]["stock"] -= quantity

            print(f"Order placed! Total: {total}")

            if cname not in orders:
                orders[cname] = []

            orders[cname].append({
                "product": products[pid]["name"],
                "quantity": quantity,
                "total": total
            })

        else:
            print("Insufficient Stock")

    else:
        print("Product Not found")


def view_orders():

    if not orders:
        print("No orders Placed")

    else:

        for cname, orders_list in orders.items():

            print(f"\nOrders for {cname}:")

            for order in orders_list:

                print(
                    f"- {order['product']} x "
                    f"{order['quantity']} = {order['total']}"
                )


def menu():

    while True:

        print("\n------ E-commerce Application ------")
        print("1. Add Products")
        print("2. View Products")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Export Orders to CSV")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_products()

        elif choice == "2":
            view_products()

        elif choice == "3":
            place_order()

        elif choice == "4":
            view_orders()

        elif choice == "5":
            export_orders_to_csv()

        elif choice == "6":
            print("Thank you")
            break

        else:
            print("Invalid option")


menu()