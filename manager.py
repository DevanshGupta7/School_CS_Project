from terminal_clear import clear_terminal
from variables import manager_details
import time


def manager():
    global is_loggedIn
    is_loggedIn = False
    is_SignedUp = False
    
    while True:
        while True:
            print("***Manager***\n")
            try:
                choice = input(f"1. Login?\n2. SignUp?\n(Enter 'BACK' to go back)\n")
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
            print("***Manager***\n")
            name = input("Enter your name (Enter 'BACK' to go back): ")
            if name.upper() == "BACK":
                clear_terminal()
                return
            passw = input("Enter your password (Enter 'BACK' to go back): ")
            if passw.upper() == "BACK":
                clear_terminal()
                return
            for stored_details in manager_details:
                if stored_details[0] == name and stored_details[1] == passw:
                    is_loggedIn = True
                    print("Login successfull")
                    clear_terminal()
                    break

            if is_loggedIn == False:
                print("Inputed credentials are wrong.")
                time.sleep(2)
                clear_terminal()
                continue
            else:
                from manage_plans_manager import manage_plans
                manage_plans()
            break

        elif choice == 2:
            print("***Manager***\n")
            name_signup = input("Enter your name (Enter 'BACK' to go back): ")
            if name_signup.upper() == "BACK":
                clear_terminal()
                return
            email_id = input("Enter your emailID (Enter 'BACK' to go back): ")
            if email_id.upper() == "BACK":
                clear_terminal()
                return
            passw_signup = input("Enter your password (Enter 'BACK' to go back): ")
            if passw_signup.upper() == "BACK":
                clear_terminal()
                return
            mobile_no = input("Enter your mobile number (Enter 'BACK' to go back): ")
            if mobile_no.upper() == "BACK":
                clear_terminal()
                return
            else:
                mobile_no = int(mobile_no)
            manager_details.append([[name_signup, passw_signup], email_id, mobile_no])
            print("Successfully Signed Up")
            time.sleep(2)
            clear_terminal()
            continue