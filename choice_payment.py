from variables import memberships, memberships_plans
from terminal_clear import clear_terminal
from datetime import datetime, timedelta
from choose_plan import plan_choose
import time


def payment_choice(costmr_id, money_pay, month):
    while True:
        while True:
            print("***Costumer***\n")
            try:
                choice = input(f"1. Debit Card?\n2. Credit Card?\n3. UPI\n4. Cash\n(Enter 'BACK' to go back\n)")
                if choice.upper() == "BACK":
                    plan_choose(memberships_plans, costmr_id)
                else:
                    choice = int(choice)
                if choice > 5:
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
            confirm = input("Do you want to confirm it: ")
            if confirm.upper() == "YES":
                while True:
                    try:
                        debit_no = int(input("Enter Debit Card number: "))
                        if len(str(debit_no)) == 12:
                            break
                        else:
                            continue
                    except ValueError:
                        print("Pls enter only integers")
                        time.sleep(2)
                        continue
                    
                print("Money is debited from your bank account")
                current_date = datetime.now().date()
                date_after_plan = current_date+timedelta(days=month*30)
                memberships[costmr_id]["plan"] = "deluxe"
                memberships[costmr_id]["start_date"] = current_date
                memberships[costmr_id]["end_date"] = date_after_plan
                memberships[costmr_id]["Membership"] = "YES"
            else:
                continue
            
        elif choice == 2:
            confirm = input("Do you want to confirm it: ")
            if confirm.upper() == "YES":
                while True:
                    try:
                        debit_no = int(input("Enter Credit Card number: "))
                        if len(str(debit_no)) == 12:
                            break
                        else:
                            continue
                    except ValueError:
                        print("Pls enter only integers")
                        time.sleep(2)
                        continue
                        
                print("Money is debited from your bank account")
                current_date = datetime.now().date()
                date_after_plan = current_date+timedelta(days=month*30)
                memberships[costmr_id]["plan"] = "deluxe"
                memberships[costmr_id]["start_date"] = current_date
                memberships[costmr_id]["end_date"] = date_after_plan
                memberships[costmr_id]["Membership"] = "YES"
            else:
                continue
            
        elif choice == 3:
            confirm = input("Do you want to confirm it: ")
            if confirm.upper() == "YES":
                upi = input("Enter UPI id: ")
                print("Money is debited from your bank account")
                current_date = datetime.now().date()
                date_after_plan = current_date+timedelta(days=month*30)
                memberships[costmr_id]["plan"] = "deluxe"
                memberships[costmr_id]["start_date"] = current_date
                memberships[costmr_id]["end_date"] = date_after_plan
                memberships[costmr_id]["Membership"] = "YES"
            else:
                continue
            
        elif choice == 4:
            confirm = input("Do you want to confirm it: ")
            if confirm.upper() == "YES":
                while True:
                    try:
                        cash = int(input("Pls enter amount to pay: "))
                        
                        if money_pay == cash:
                            break
                        else:
                            print(f"Pls pay only {money_pay} rupees")
                            continue
                    except ValueError:
                        print("Pls enter only integers")
                        time.sleep(2)
                        continue
                        
                print("Successfully cash recieved")
                current_date = datetime.now().date()
                date_after_plan = current_date+timedelta(days=month*30)
                memberships[costmr_id]["plan"] = "deluxe"
                memberships[costmr_id]["start_date"] = current_date
                memberships[costmr_id]["end_date"] = date_after_plan
                memberships[costmr_id]["Membership"] = "YES"
            else:
                continue
