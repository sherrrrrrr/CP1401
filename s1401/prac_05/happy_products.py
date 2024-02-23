def calculate_price(num_products, price):
    if num_products < 0 or price <= 0:
        return "Invalid input"

    if num_products <= 5:
        total_price = num_products * price
    else:
        total_price = num_products * price * 0.9

    return f"{num_products} x ${price:.2f} products = ${total_price:.2f}"


def print_instructions():
    print("Enter the number of products you want to buy and your chosen price.")
    print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")


def main():
    while True:
        print("Menu:")
        print("(I)nstructions")
        print("(C)alculate")
        print("(Q)uit")

        choice = input("Choice: ").lower()

        if choice == "i":
            print_instructions()
        elif choice == "c":
            num_products = -1
            price = -1.0

            while num_products < 0 or price <= 0:
                num_products = int(input("Number of products: "))
                price = float(input("Price: "))

                if num_products < 0 or price <= 0:
                    print("Invalid input")

            result = calculate_price(num_products, price)
            print(result)
        elif choice == "q":
            print("Farewell")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()








