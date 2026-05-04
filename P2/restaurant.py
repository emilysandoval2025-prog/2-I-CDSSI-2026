#CAFE
#EMILY SANDOVAL MADERO 2'I 12 de marzo de 2026
#Menu

beverages = {
    "A": {"n": "Expreso", "c": 5.00},
    "B": {"n": "Double expreso", "c": 5.00},
    "C": {"n": "Iced latte", "c": 5.00},
    "D": {"n": "Americano", "c": 7.00},
    "E": {"n": "Macchiato", "c": 8.00},
    "F": {"n": "Flat white", "c": 9.00},
    "G": {"n": "Cappuccino", "c": 10.00},  # Fixed typo
}
#Sizes
Small = 1.50
Medium = 2.00
Big = 3.00

# Storage for reservations and orders
reservations = []
orders = []

while True:
    print("Hello, welcome to our Cafe, which service would you like?")
    print("1-Add beverage to menu")
    print("2-Make a reservation")
    print("3-Take customer orders.")
    print("4-Show the menu.")
    print("5-Show the list of reservations.")
    print("6-Show the orders.")
    print("7-Exit")
    option = int(input(" "))

    match option:
        case 1:
            name = input("Introduce the name: ")
            cost = float(input("Which costs? "))  # Convert to float
            last_key = list(beverages.keys())[-1]
            beverages[chr(ord(last_key[0]) + 1)] = {"n": name, "c": cost}
            print(beverages)
        case 2:
            date = input("What date would you like to reserve (dd/mm): ")
            time = input("What time would you like to reserve? (00:00): ")
            owner = input("Under what name would it be for: ")
            persons = int(input("How many people would be coming to the table? Including yourself: "))  # Convert to int
            reservation = {"date": date, "time": time, "owner": owner, "persons": persons}
            reservations.append(reservation)
            print("Your reservation has been saved for the date", date, "at", time, "for", owner, "and a table for", persons)
        case 3:
            for clave, valor in beverages.items():
                print(f"{clave}, {valor['n']} ${valor['c']}")

            order = input("What would you like to order? (Enter key like A): ").upper()
            if order not in beverages:
                print("Invalid order key.")
            else:
                customer = input("Under what name will it be for?: ")
                place = input("Will this be for here, or on the go? (Take out/Here): ")
                size = input("What size coffee? (small/medium/big): ").lower()

                if size == "small":
                    size_price = Small
                elif size == "medium":
                    size_price = Medium
                elif size == "big":
                    size_price = Big
                else:
                    print("Sorry, we don't have that size.")
                    size_price = 0

                base_price = beverages[order]["c"]
                price = base_price + size_price
                if price > 0:
                    print(f"One {size} {beverages[order]['n']} coming up! That'll be ${price:.2f}.")
                    order_data = {"customer": customer, "order": order, "size": size, "price": price, "place": place}
                    orders.append(order_data)
        case 4:
            print("Menu:")
            for clave, valor in beverages.items():
                print(f"{clave}: {valor['n']} - ${valor['c']:.2f}")
        case 5:
            print("Reservations:")
            if not reservations:
                print("No reservations yet.")
            else:
                for res in reservations:
                    print(f"Date: {res['date']}, Time: {res['time']}, Owner: {res['owner']}, Persons: {res['persons']}")
        case 6:
            print("Orders:")
            if not orders:
                print("No orders yet.")
            else:
                for ord in orders:
                    print(f"Customer: {ord['customer']}, Order: {ord['order']} ({ord['size']}), Price: ${ord['price']:.2f}, Place: {ord['place']}")
        case 7:
            print("Thank you for your patience,your service will be ready soon!")
            break
        case _:
            print("Invalid option.")