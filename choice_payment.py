from variables import memberships, memberships_plans
from terminal_clear import clear_terminal
from datetime import datetime, timedelta
import time


def payment_choice(costmr_id, money_pay, month, buyed_plan):
    while True:
        print("***Costumer***\n")
        try:
            choice = input(f"1. Debit Card?\n2. Credit Card?\n3. UPI\n4. Cash\n(Enter 'BACK' to go back)\n")
            if choice.upper() == "BACK":
                clear_terminal()
                from choose_plan import plan_choose
                plan_choose(memberships_plans, costmr_id)
            else:
                choice = int(choice)
            if choice > 5:
                print("Pls choose only from given options")
                time.sleep(2)
                clear_terminal()
                continue
            else:
                break
        except ValueError:
            print("Pls input integer for choice. Wait for 2 seconds")
            time.sleep(2)
            clear_terminal()
            
            
    if choice == 1:
        clear_terminal()
        confirm = input("Do you want to confirm it: ")
        if confirm.upper() == "YES":
            while True:
                try:
                    debit_no = int(input("Enter Debit Card number: "))
                    if len(str(debit_no)) == 12:
                        break
                    else:
                        print("Pls enter 12 digits debit card number")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Pls enter only integers")
                    time.sleep(2)
                    continue
                
            print("Money is debited from your bank account")
            current_date = datetime.now().date()
            date_after_plan = current_date+timedelta(days=month*30)
            current_date = current_date.strftime("%Y%m%d")
            date_after_plan = date_after_plan.strftime("%Y%m%d")
            
            memberships[costmr_id]["plan"] = buyed_plan
            memberships[costmr_id]["start_date"] = current_date
            memberships[costmr_id]["end_date"] = date_after_plan
            memberships[costmr_id]["Membership"] = "YES"
            print(type(memberships[costmr_id]["end_date"]))
            print(type(datetime.now().date()))
            print(memberships)
            
            current_date = datetime.strptime(current_date, "%Y%m%d").date()
            formatted_current_date = datetime(current_date.year, current_date.month, current_date.day).date()
            date_after_plan = datetime.strptime(date_after_plan, "%Y%m%d").date()
            formatted_dayafterplan_date = datetime(date_after_plan.year, date_after_plan.month, date_after_plan.day).date()
            
            print(f"Plan is: {buyed_plan}\nPrice is: {money_pay}\nStart date is: {formatted_current_date}\nEnd date is:{formatted_dayafterplan_date}")
            enter = input("Press any key and tap enter to continue: ")
            if len(enter) != 0:
                clear_terminal()
                from customer_login import choose_customer
                choose_customer()
                return
        else:
            payment_choice()
            return
        
    elif choice == 2:
        clear_terminal()
        confirm = input("Do you want to confirm it: ")
        if confirm.upper() == "YES":
            while True:
                try:
                    debit_no = int(input("Enter Credit Card number: "))
                    if len(str(debit_no)) == 12:
                        break
                    else:
                        print("Pls enter 12 digits debit card number")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Pls enter only integers")
                    time.sleep(2)
                    continue
                    
            print("Money is debited from your bank account")
            current_date = datetime.now().date()
            date_after_plan = current_date+timedelta(days=month*30)
            current_date = current_date.strftime("%Y%m%d")
            date_after_plan = date_after_plan.strftime("%Y%m%d")
            
            memberships[costmr_id]["plan"] = buyed_plan
            memberships[costmr_id]["start_date"] = current_date
            memberships[costmr_id]["end_date"] = date_after_plan
            memberships[costmr_id]["Membership"] = "YES"
            print(memberships)
            print(f"Plan is: {buyed_plan}\nPrice is: {money_pay}\nStart date is: {current_date}\nEnd date is:{date_after_plan}")
            enter = input("Press any key and tap enter to continue: ")
            if len(enter) != 0:
                clear_terminal()
                from customer_login import choose_customer
                choose_customer()
                return
        else:
            payment_choice()
            return 
        
    elif choice == 3:
        clear_terminal()
        confirm = input("Do you want to confirm it: ")
        if confirm.upper() == "YES":
            upi = input("Enter UPI id: ")
            print("Money is debited from your bank account")
            current_date = datetime.now().date()
            date_after_plan = current_date+timedelta(days=month*30)
            current_date = current_date.strftime("%Y%m%d")
            date_after_plan = date_after_plan.strftime("%Y%m%d")
            
            memberships[costmr_id]["plan"] = buyed_plan
            memberships[costmr_id]["start_date"] = current_date
            memberships[costmr_id]["end_date"] = date_after_plan
            print(memberships)
            print(f"Plan is: {buyed_plan}\nPrice is: {money_pay}\nStart date is: {current_date}\nEnd date is:{date_after_plan}")
            enter = input("Press any key and tap enter to continue: ")
            if len(enter) != 0:
                clear_terminal()
                from customer_login import choose_customer
                choose_customer()
                return
            payment_choice()
            return
        
    elif choice == 4:
        clear_terminal()
        confirm = input("Do you want to confirm it: ")
        if confirm.upper() == "YES":
            while True:
                try:
                    print(f"Amount to pay is {money_pay}")
                    cash = int(input("Pls enter amount to pay: "))
                    
                    if money_pay == cash:
                        clear_terminal()
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
            current_date = current_date.strftime("%Y%m%d")
            date_after_plan = date_after_plan.strftime("%Y%m%d")
            
            memberships[costmr_id]["plan"] = buyed_plan
            memberships[costmr_id]["start_date"] = current_date
            memberships[costmr_id]["end_date"] = date_after_plan
            memberships[costmr_id]["Membership"] = "YES"
            print(memberships)
            print(f"Plan is: {buyed_plan}\nPrice is: {money_pay}\nStart date is: {current_date}\nEnd date is:{date_after_plan}")
            enter = input("Press any key and tap enter to continue: ")
            if len(enter) != 0:
                clear_terminal()
                from customer_login import choose_customer
                choose_customer()
                return
        else:
            payment_choice()
            return
            
            
