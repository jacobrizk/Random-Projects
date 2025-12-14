# Spend Bill Gate's Money attempt
import tkinter as tk

bg_money = 104800000000

items = {
    "Universial Studios": 2700000000,
    "Shark": 200000,
    "Butler" : 70000,
    "Nerds Gummy": 4,
    "DrPepper": 2,
    "Fudruckers": 470000,
    "End World Hunger": 207000000000,
    "Generic Laptop": 500,
    "Onbrand Laptop": 2000,
    "Sour Skittles": 3,
}

wind = tk.Tk()

wind.title("Spend ts money")

while bg_money > 0:
    user = input("what would you like? ")

    if user in items:
        price = items[user]
    else:
        print("not in list")

    bg_money = bg_money - price

    print(bg_money)

print("You're Broke Dumbass")