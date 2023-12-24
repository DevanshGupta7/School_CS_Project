from terminal_clear import clear_terminal
import time


def plan_choose(memberships_plans, costmr_id):
    print("You dont have any valid membership pls buy to continue")
    
    from table_print import print_table_plan
    print_table_plan(memberships_plans)
    print("\n")
    print("Deluxe:\nAccess to gym facilities, Standard workout equipment usage (cardio machines, weightlifting equipment), general fitness classes\n\nSuper:\nAll benefits of Deluxe Membership, Access to additional amenities, such as sauna or steam room, Extended gym hours, Personalized fitness assessment\n\nPremium:\nAll benefits of Super Membership, Access to premium gym equipment and technology, Unlimited access to all fitness classes, including specialty classes, Personalized workout plans designed by fitness trainers, Nutrition consultation")
    print("NO REFUND POLICY")
    
    while True:
        print("***Welcome to GYM***\n")
        try:
            plan = int(input("1. Deluxe\n2. Super\n3. Premium\n"))
            if plan > 3:
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
    
    if plan == 1:
        confirm = input("Do want to confirm it: ")
        if confirm.upper() == "YES":
            month = int(input("Duration of membership in month: "))
            money_pay = (800*month) - (800*month)*(month/100)
            print(f"Original money is {month*800}\nDiscounted money is {money_pay}")
            buyed_plan = "Deluxe"
        else:
            clear_terminal()
            plan_choose(memberships_plans, costmr_id)
            return
    elif plan == 2:
        confirm = input("Do want to confirm it: ")
        if confirm.upper() == "YES":
            month = int(input("Duration of membership in month: "))
            money_pay = (1500*month) - (1500*month)*(month/100)
            print(f"Original money is {month*1500}\nDiscounted money is {money_pay}")
            buyed_plan = "Super"
        else:
            clear_terminal()
            plan_choose(memberships_plans, costmr_id)
            return
    elif plan == 3:
        confirm = input("Do want to confirm it: ")
        if confirm.upper() == "YES":
            month = int(input("Duration of membership in month: "))
            money_pay = (2000*month) - (2000*month)*(month/100)
            print(f"Original money is {month*2000}\nDiscounted money is {money_pay}")
            buyed_plan = "Premium"
        else:
            clear_terminal()
            plan_choose(memberships_plans, costmr_id)
            return
        
    from choice_payment import payment_choice
    payment_choice(costmr_id, money_pay, month, buyed_plan)
