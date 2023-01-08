items = {
    "A": {"name": "lolipop", "price": 0.25},
    "B": {"name": "Chips", "price": 2.0},
    "C": {"name": "7UP", "price": 4.0},
    "D": {"name": "pepsi", "price": 4.0},
    "E": {"name": "Jelly", "price": 1.0},
    "F": {"name": "water", "price": 1.0},
    "G": {"name": "biscuit", "price": 1.5},
    "H": {"name": "redbull", "price": 12.0},
    "I": {"name": "Energybar", "price": 1.0},
    "J": {"name": "ved sandwich", "price": 1.5},
    "K": {"name": "chicken sandwich", "price": 1.5},
    "L": {"name": "icecream", "price": 1.5},
    "M": {"name": "ice lolly", "price": 0.50},
    }

balance = 10

while True:
    print("Welcome to the vending machine!")
    print("Please select an item:")
    for key, value in items.items():
        print(f"{key}: {value['name']} ({value['price']})")

    selection = input("Enter your selection: ")
    if selection in items:
        cost = items[selection]["price"]
        if balance < cost:
            print("You do not have enough money. Please insert more money.")
        else:
            balance -= cost
            print(f"You have purchased {items[selection]['name']} for {cost}. Your balance is {balance}.")
            print("Thank you for using vending machine")
    else:
        print("Invalid selection. Please try again.")
        print("Thankyou")