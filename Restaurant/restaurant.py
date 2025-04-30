import os
import random
import create_pattern as cp

os.chdir(r"E:\Python\PracticeSet\NAVTCC\restaurant")
admin = {"name": "urooj", "pin": 124}

# menu dictionary
restaurant = {
    "Breakfast": [
        {"id": 1, "name": "Omelette", "price": 100},
        {"id": 2, "name": "Paratha", "price": 100},
        {"id": 3, "name": "Tea", "price": 50},
        {"id": 4, "name": "Coffee", "price": 100},
        {"id": 5, "name": "Halwa Puri", "price": 200}
    ],
    "Chinese": [
        {"id": 6, "name": "Chowmein", "price": 1000},
        {"id": 7, "name": "Chicken Fried Rice", "price": 800},
        {"id": 8, "name": "Shashlik", "price": 1300},
        {"id": 9, "name": "Momos", "price": 400},
        {"id": 10, "name": "Ramen", "price": 1200}
    ],
    "Starters": [
        {"id": 11, "name": "Chicken Wings", "price": 600},
        {"id": 12, "name": "Spring Rolls", "price": 500},
        {"id": 13, "name": "Cheese Balls", "price": 550}
    ],
    "Desi": [
        {"id": 14, "name": "Biryani", "price": 900},
        {"id": 15, "name": "Nihari", "price": 1200},
        {"id": 16, "name": "Haleem", "price": 1000},
        {"id": 17, "name": "Paye", "price": 1300}
    ],
    "Sweets": [
        {"id": 18, "name": "Fudge Cake", "price": 1600},
        {"id": 19, "name": "Brownie", "price": 400},
        {"id": 20, "name": "Black Forest Cake", "price": 1400},
        {"id": 21, "name": "Gulab Jamun", "price": 300}
    ],
    "Drinks": [
        {"id": 22, "name": "Mountain Dew", "price": 150},
        {"id": 23, "name": "Mojito", "price": 350}
    ],
    "Chicken Special": [
        {"id": 24, "name": "Chicken Handi", "price": 1200},
        {"id": 25, "name": "Chicken Karahi", "price": 1400}
    ],
    "Bar BQ": [
        {"id": 26, "name": "Chicken Tikka", "price": 500},
        {"id": 27, "name": "Beef Seekh Kebab", "price": 600},
        {"id": 28, "name": "Chicken Malai Boti", "price": 700}
    ],
    "Salad": [
        {"id": 29, "name": "Russian Salad", "price": 450},
        {"id": 30, "name": "Green Salad", "price": 250}
    ]
}

def update_menu_file():
    menuItems = ""
    for cat, items in restaurant.items():
        menuItems += f"\n{cat}:\n------------------------------------------\n"
        for item in items:
            menuItems += f"{item['id']}: {item['name']} ...... Price: {item['price']}\n"
    with open("menu.txt", "w") as resFile:
        resFile.write(menuItems)

update_menu_file()

def readMenu():
    print("\n\n************ Restaurant Menu ************\n")
    with open("menu.txt", "r") as file:
        res_menu = file.read()
        print(res_menu)

def admin_auth(func):
    def check(*args, **kwargs):
        admin_name = input("Enter your name: ")
        try:
            admin_pin = int(input("Enter your pin code: "))
            if admin['name'] != admin_name:
                print("❌ Username is wrong")
            elif admin['pin'] != admin_pin:
                print("❌ Pin is wrong")
            else:
                func(*args, **kwargs)
        except ValueError:
            print("❌ Invalid input for pin!")
    return check

# Main Code
print("\t\t\t\t\t\tWelcome To")
var = cp.word("Restaurant", "*")

user = input("Are you admin or user? Enter below:\n")

if user.lower() == "admin":
    @admin_auth
    def admin():
        while True:
            try:
                admin_input = int(input('''\nDo you want to 
    1: View Menu
    2: Add item to Menu
    3: Remove Item From Menu
    4: Update Item in Menu
    5: View Customer Details
    6: Exit
    '''))

                if admin_input == 1:
                    readMenu()
                elif admin_input == 2:
                    n_cat = input("Enter Category: ")
                    n_id = int(input("Enter Item ID: "))
                    n_name = input("Enter Item Name: ")
                    n_price = int(input("Enter Item Price: "))
                    new_item = {"id": n_id, "name": n_name, "price": n_price}
                    if n_cat in restaurant:
                        restaurant[n_cat].append(new_item)
                        print(f"✅ Added to existing category: {n_cat}")
                    else:
                        restaurant[n_cat] = [new_item]
                        print(f"✅ New category '{n_cat}' created and item added")
                    update_menu_file()

                elif admin_input == 3:
                    rId = int(input("Enter id to remove item: "))
                    found = False
                    for cat, items in restaurant.items():
                        for item in items:
                            if item['id'] == rId:
                                items.remove(item)
                                print("✅ Item removed successfully")
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        print("❌ ID not found!")
                    update_menu_file()

                elif admin_input == 4:
                    update_ask = input("Update price or name? Enter 'P' or 'N': ").upper()
                    u_id = int(input("Enter id to update item: "))
                    found = False
                    for cat, items in restaurant.items():
                        for item in items:
                            if item['id'] == u_id:
                                if update_ask == "P":
                                    item['price'] = int(input("Enter new price: "))
                                    print("✅ Price updated")
                                elif update_ask == "N":
                                    item['name'] = input("Enter new name: ")
                                    print("✅ Name updated")
                                else:
                                    print("❌ Invalid choice")
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        print("❌ Given ID does not exist!")
                    update_menu_file()

                elif admin_input == 5:
                    with open("userBill.txt", "r") as readbill:
                        print(readbill.read())

                elif admin_input == 6:
                    print("Exiting admin panel.")
                    break
                else:
                    print("❌ Invalid option")
            except ValueError:
                print("❌ Enter a valid number!")

    admin_menu()

elif user.lower() == "user":
    readMenu()
    order = []
    bill = ""
    total_bill = 0
    all_ids = [item['id'] for sublist in restaurant.values() for item in sublist]

    while True:
        try:
            m_id = int(input("Select item by ID (0 to finish): "))
            if m_id == 0:
                break
            if m_id not in all_ids:
                raise ValueError("❌ Invalid item ID!")
            for cat, items in restaurant.items():
                for item in items:
                    if item['id'] == m_id:
                        order.append(item)
                        bill += f"{item['name']} ---------- {item['price']} Rs\n"
                        total_bill += item['price']
                        break
        except ValueError as e:
            print(e)

    if order:
        cusId = f"cus{random.randint(1000,9999)}"
        with open("userBill.txt", "a") as userBill:
            userBill.write("\n***** Customer Bill *****\n")
            userBill.write(f"Customer ID: {cusId}\n")
            userBill.write("Item Names\t\tPrice\n")
            userBill.write(bill)
            userBill.write(f"\nTotal Bill: {total_bill} Rs\n")

        print("\n***** Your Bill *****")
        print("Item Names\t\tPrice")
        print(bill)
        print(f"\nTotal Bill: {total_bill} Rs")
    else:
        print("❌ No items ordered.")

else:
    print("❌ Invalid user type. Enter 'admin' or 'user'.")
