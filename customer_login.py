import time
import random
from terminal_clear import clear_terminal
from variables import memberships, memberships_plans, costumer_details
from datetime import datetime


def choose_customer():
    while True:
        print("***Welcome to GYM***\n")
        try:
            choice = input(f"1. Existing customer?\n2. New customer?\n(Enter 'BACK' for going back)\n")
            if choice.upper() == "BACK":
                from user_choose import choose_user
                choose_user()
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
        is_costumer_valid = False
        costmr_id = int(input("Enter your id: "))
        back_continue = int(input("1. Continue\n2. Back\n"))

        if back_continue == 2:
            clear_terminal()
            choose_customer()
            return
        elif choice != 1 and choice != 2:
            print("Pls enter only from above options")
            time.sleep(2)
            choose_customer()
            
        if costmr_id in memberships:
            if memberships[costmr_id]["end_date"] < datetime.now().date().strftime("%Y%m%d") or len(memberships[costmr_id]["end_date"]) == 0:
                memberships[costmr_id]["Membership"] = "NO"
                
                if memberships[costmr_id]["Membership"] == "NO":
                    clear_terminal()
                    from choose_plan import plan_choose
                    plan_choose(memberships_plans, costmr_id)
                else:
                    print("Welcome to GYM")
                    is_costumer_valid = True
                    
            else:
                print("Welcome to GYM")
                is_costumer_valid = True
                
        else:
            print("Pls enter correct ID or register to our GYM")
            time.sleep(2)
            clear_terminal()
            choose_customer()
            return
            
        if is_costumer_valid:
            print("You have valid membership. So, please continue to GYM\nEnjoy your Day!")
            print(f"Your plan will on {memberships[costmr_id]["end_date"]}")
            
    elif choice == 2:
        print("Register yourself in our GYM\n")
        name = input("Enter your name: ")
        address = input("Enter your address: ")

        while True:
            try:
                contact = int(input("Enter your contact number: "))
                back_continue = int(input("1. Continue\n2. Back\n"))
                if back_continue == 1:
                    break
                elif back_continue == 2:
                    clear_terminal()
                    choose_customer()
                    return
                else:
                    print("Pls enter only from above options")
                    time.sleep(2)
                    choose_customer()
                
                if len(str(contact)) != 10:
                    print("Pls enter 10-digit mobile number!")
                    continue
                else:
                    break

            except ValueError:
                print("Pls enter only integers")
                continue

        while True:
            costumer_ID = random.randint(100000, 999999)
            if costumer_ID not in costumer_details:
                costumer_details[costumer_ID] = {
                    "name": name, "address": address, "contact": contact}
                memberships[costumer_ID] = {
                    "Membership": "NO", "plan":"", "start_date": "", "end_date": ""}
                from table_print import print_table_costumer
                clear_terminal()
                print_table_costumer(costumer_details, costumer_ID)
                enter = input("Press any key and tap enter to continue: ")
                if len(enter) != 0:
                    clear_terminal()
                    choose_customer()
                    return
            
            