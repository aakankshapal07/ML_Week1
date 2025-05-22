#  Cafe Management

menu = {
    "Coffee": 5.0,
    "Tea": 5.0,
    "Sandwich": 30.0,
    "Cake": 60.0,
    "Juice": 40.0,
}

order = {}

def display_menu():
    print("\n--- Cafe Menu ---")
    for item, price in menu.items():
        print(f"{item}: {price:.2f}")

def take_order():
    while True:
        item = input("Enter item name to order (or 'done' to finish): ").title()
        if item == 'Done':
            break
        if item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not found in the menu.")

def generate_bill():
    print("\n--- Bill ---")
    total = 0
    for item, quantity in order.items():
        price = menu[item]
        subtotal = price * quantity
        total += subtotal
        print(f"{item} x {quantity} = {subtotal:.2f}")
    print(f"\nTotal amount: {total:.2f}")
    print("Thank you for visiting!")

def main():
    print("Welcome to code Cafe!")
    display_menu()
    take_order()
    generate_bill()

if __name__ == "__main__":
    main()

