def calculate_price(number_of_products, product_price):
    if number_of_products < 0 or product_price <= 0:
        return "Invalid input"

    if number_of_products <= 5:
        total_price = number_of_products * product_price
    else:
        total_price = number_of_products * product_price * 0.9

    return f"{number_of_products} x ${product_price:.2f} products = ${total_price:.2f}"

def main():
    while True:
            print("Menu:")
            print("(I)nstructions")
            print("(C)alculate")
            print("(Q)uit")

            choice = input("Choice: ").lower()

            if choice == "i":
                print("Enter the number of products you want to buy and your chosen price.")
                print("If you buy 0-5 items, they're full price, "
                      "over 5 items and each one is 10% off!")
            elif choice == "c":
                num_products = int(input("Number of products: "))
                price = float(input("Price: "))
                result = calculate_price(number_of_products, product_price)
                print(result)
            elif choice == "q":
                print("Farewell")
                break
            else:
                print("Invalid choice")







