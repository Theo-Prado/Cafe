print(".....Canelinha Cafe.....")
print(".......since 1980.......")
print()

name = input("Enter your name: ")
print()
print("Hello,", name+"!", "Welcome to Canelinha Cafe!")
print()

options = {
    "cappuccino": [12, 10],
    "frappuccino": [12, 10],
    "moccaccino": [12, 10],
    "macchiato": [12, 10],
    "latte": [10, 10],
    "espresso": [7, 10],
    "espresso latte": [9, 10]
}

users = {}
cart = {}

discount = False
running = True


# ---------------- CPF VALIDATION ----------------
def validate_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)

    digit1 = (total * 10) % 11
    if digit1 == 10:
        digit1 = 0

    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)

    digit2 = (total * 10) % 11
    if digit2 == 10:
        digit2 = 0

    return digit1 == int(cpf[9]) and digit2 == int(cpf[10])


# ---------------- CART ----------------
def show_cart(cart, options, discount):
    if not cart:
        print("Cart is empty.")
        return

    total = 0

    for item in cart:
        qty = cart[item]
        price = options[item][0]
        subtotal = qty * price
        total += subtotal
        print(f"- {item} x{qty} = $ {subtotal}")

    if discount:
        print("Total with discount: $", total * 0.9)
    else:
        print("Total: $", total)


# ---------------- ADMIN ----------------
def admin_menu(options):
    admin_running = True

    while admin_running:
        print("\n--- ADMIN MENU ---")
        counter = 1
        item_list = list(options.keys())

        for coffee in item_list:
            print(counter, "-", coffee, "| Stock:", options[coffee][1])
            counter += 1

        print("1 - Change stock")
        print("2 - Add stock")
        print("3 - Reset stock")
        print("0 - Exit admin")

        choice = int(input("Choice: "))

        if choice == 0:
            admin_running = False

        elif choice in [1, 2, 3]:
            while True:
                try:
                    item = int(input("Enter product number: "))
                    if 1 <= item <= len(item_list):
                        break
                    else:
                        print(f"Invalid number. Choose between 1 and {len(item_list)}.")
                except ValueError:
                    print("Invalid input. Enter a number.")

            coffee = item_list[item - 1]

            if choice == 1:
                new_value = int(input("New stock value: "))
                options[coffee][1] = new_value
                print("Stock updated!")

            elif choice == 2:
                add = int(input("Amount to add: "))
                options[coffee][1] += add
                print("Stock added!")

            elif choice == 3:
                options[coffee][1] = 0
                print("Stock reset!")

        else:
            print("Invalid option.")


# ---------------- MAIN MENU ----------------
while running:
    counter = 1
    for coffee in options:
        print(counter, "-", coffee, "$", options[coffee][0], "| Stock:", options[coffee][1])
        counter += 1

    print("9 - View cart")
    print("10 - Register")
    print("11 - Login")
    print("12 - Remove item")
    print("0 - Finish")
    print()

    choice = int(input("Choice: "))
    print()

    if choice == 0:
        show_cart(cart, options, discount)
        print("Thanks for your purchase!")
        break

    elif 1 <= choice <= len(options):
        item_list = list(options.keys())
        coffee = item_list[choice - 1]

        qty = int(input("Quantity: "))
        stock = options[coffee][1]

        if qty <= stock and qty > 0:
            cart[coffee] = cart.get(coffee, 0) + qty
            options[coffee][1] -= qty
            print("Item added!")
        else:
            print("Insufficient stock!")

    elif choice == 9:
        show_cart(cart, options, discount)

    elif choice == 10:
        username = input("Create a username: ")

        if username in users:
            print("Username already exists.")
            continue

        password = input("Create a password: ")
        confirm = input("Confirm password: ")

        if password != confirm:
            print("Passwords do not match.")
            continue

        cpf = input("Enter your CPF: ")

        if not validate_cpf(cpf):
            print("Invalid CPF.")
            continue

        users[username] = {"password": password, "cpf": cpf}
        print("Registration successful! Discount applied.")
        discount = True

    elif choice == 11:
        username = input("Username: ")
        password = input("Password: ")

        # ADMIN LOGIN
        if username == "admin" and password == "admin@155":
            print("ADMIN login successful!")
            admin_menu(options)

        # NORMAL LOGIN
        elif username in users and users[username]["password"] == password:
            print("Login successful!")
            discount = True

        else:
            print("Incorrect username or password.")

    elif choice == 12:
        item_list = list(options.keys())

        item_choice = int(input("Item number: "))
        coffee = item_list[item_choice - 1]

        if coffee not in cart:
            print("Item not in cart.")
        else:
            qty = int(input("Quantity to remove: "))

            if qty >= cart[coffee]:
                options[coffee][1] += cart[coffee]
                del cart[coffee]
            else:
                cart[coffee] -= qty
                options[coffee][1] += qty

            print("Item removed successfully!")

    else:
        print("Invalid option.")

    print()
