from variables import memberships_plans
from terminal_clear import clear_terminal
import time

def show_alldetails():
    pass


def manage_plans():
    while True:
        while True:
            print("Do you want to change price of membership plans?\n")
            try:
                choice = input(f"1. Deluxe?\n2. Super\n2. Premium?\n(Enter 'BACK' to go back)\n")
                if choice.upper() == "BACK":
                    from manager import manager
                    manager()
                else:
                    choice = int(choice)
                    
                if choice > 3:
                    print("Pls choose only from given options")
                    time.sleep(2)
                    clear_terminal()
                    continue
                else:
                    clear_terminal()
                    break
            except ValueError:
                print("Pls input integer for choice. Wait for 2 seconds")
                time.sleep(2)
                clear_terminal()
                
        if choice == 1:
            price = input("Enter new cost for Deluxe membership (Enter 'BACK' to go back): ")
            if price.upper() == "BACK":
                clear_terminal()
                return
            else:
                price = int(price)
            memberships_plans["1"]["price"] = price
            print(memberships_plans)
        if choice == 2:
            price = input("Enter new cost for Super membership (Enter 'BACK' to go back): ")
            if price.upper() == "BACK":
                clear_terminal()
                return
            else:
                price = int(price)
            memberships_plans["2"]["price"] = price
            print(memberships_plans)
        if choice == 3:
            price = input("Enter new cost for Deluxe membership (Enter 'BACK' to go back): ")
            if price.upper() == "BACK":
                clear_terminal()
                return
            else:
                price = int(price)
            memberships_plans["3"]["price"] = price
            print(memberships_plans)
            
            