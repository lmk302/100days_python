MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made,
    False if ingredients are insufficient"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted,
     or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappucchino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
























# ingredient = {"water": 300, "milk": 200, "coffee":100}
# espresso = {"price": 1.5, "water": 50, "coffee": 18}
# latte = {"price": 2.5, "water": 200, "milk":150, "coffee":24}
# cappuccino = {"price": 3, "water": 250, "milk":100, "coffee":24}


# def report():
#     print(f"Water: {ingredient['water']}ml")
#     print(f"Milk: {ingredient['milk']}ml")
#     print(f"Coffee: {ingredient['coffee']}g")
#     print(f"Money: $ 0")

# def check_stock(user_input):
#     print (type(ingredient["water"]))
#     print("------")
#     print(user_input)
#     print (type(user_input["water"]))
    
    # if ingredient["water"] <= user_input["water"] or ingredient["milk"] <= user_input["milk"] or ingredient["coffee"] <= user_input["coffee"]:
    #     print("there is not enough ingredient")
    # else:
    #     ingredient["water"] -= user_input["water"] 
    #     ingredient["milk"] -= user_input["milk"] 
    #     ingredient["coffee"] -= user_input["coffee"]
    #     print(f"here is your {user_input}")


# # three flavors
# # coin operated
# # input
# user_input = input("What would you like? (espresso/latte/cappuccino): ")

# # report
# if user_input == "report":
#     report()
# elif user_input == ("espresso" or "latte" or "cappuccino"):
#     check_stock(user_input)