from terminal_clear import clear_terminal
import time
from variables import memberships, memberships_plans
from datetime import datetime
from choose_plan import plan_choose


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
            #egister_user(costumer_details, memberships)
            pass
            
            