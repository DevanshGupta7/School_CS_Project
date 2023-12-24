import time
import random
from terminal_clear import clear_terminal
from variables import memberships, memberships_plans, costumer_details
from datetime import datetime


def choose_customer():
    while True:
        while True:
            print("***Welcome to GYM***\n")
            try:
                choice = input(f"1. Existing costumer?\n2. New costumer?\n(Enter 'BACK' for going back)\n")
                if choice.upper() == "BACK":
                    from user_choose import choose_user
                    choose_user()
                else:
                    choice = int(choice)
                if choice > 2:
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
            while True:
                costmr_id = input("Enter your id (Enter 'BACK' for going back): ")
                if costmr_id.upper() == "BACK":
                    clear_terminal()
                    break
                else:
                    costmr_id = int(costmr_id)
                if costmr_id in memberships:
                    if memberships[costmr_id]["end_date"] < datetime.now().date():
                        memberships[costmr_id]["Membership"] = "NO"
                        
                        if memberships[costmr_id]["Membership"] == "NO":
                            from choose_plan import plan_choose
                            plan_choose(memberships_plans, costmr_id)
                        else:
                            print("Welcome to GYM")
                            is_costumer_valid = True
                            break
                    else:
                        print("Welcome to GYM")
                        is_costumer_valid = True
                        break
                else:
                    print("Pls enter correct ID or register to our GYM")
                    continue
                
            if is_costumer_valid:
                print("You have valid membership. So, please continue to GYM")
                
        elif choice == 2:
            print("Register yourself in our GYM\n")
            while True:
                name = input("Enter your name(Enter 'BACK' for going back): ")
                if name.upper() == "BACK":
                    clear_terminal()
                    break
                address = input("Enter your address(Enter 'BACK' for going back): ")
                if address.upper() == "BACK":
                    clear_terminal()
                    break

                while True:
                    try:
                        contact = (input("Enter your contact number(Enter 'BACK' for going back): "))
                        if contact.upper() == "BACK":
                            clear_terminal()
                            return
                        else:
                            contact = int(contact)
                        if len(str(contact)) != 10:
                            print("Pls enter 10-digit mobile number!")
                            continue
                        else:
                            break

                    except ValueError:
                        print("Pls enter only integers")
                        continue

                while True:
                    is_signedUp = False
                    costumer_ID = random.randint(100000, 999999)
                    if costumer_ID not in costumer_details:
                        costumer_details[costumer_ID] = {
                            "name": name, "address": address, "contact": contact}
                        memberships[costumer_ID] = {
                            "Membership": "NO", "plan":"", "start_date": "", "end_date": ""}
                        from table_print import print_table_costumer
                        is_signedUp = True
                        print_table_costumer(costumer_details, costumer_ID)
                        enter = input("Press any key and tap enter to continue: ")
                        if len(enter) != 0:
                            break
                if is_signedUp:
                    break
            
            