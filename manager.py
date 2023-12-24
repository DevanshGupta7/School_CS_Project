from terminal_clear import clear_terminal
from variables import manager_details
import time


def manager():
    global is_loggedIn
    is_loggedIn = False
    
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
        name = input("Enter your name: ")
        passw = input("Enter your password: ")
        back_continue = int(input("1. Continue\n2. Back\n"))
        if back_continue == 2:
            clear_terminal()
            manager()
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
            manager()
        else:
            from manage_access import manage_plans
            manage_plans()

    elif choice == 2:
        print("***Manager***\n")
        name_signup = input("Enter your name: ")
        email_id = input("Enter your emailID: ")
        passw_signup = input("Enter your password: ")
        mobile_no = int(input("Enter your mobile number : "))
        back_continue = int(input("1. Continue\n2. Back\n"))
        if back_continue == 2:
            clear_terminal()
            manager()
            return
        
        manager_details.append([[name_signup, passw_signup], email_id, mobile_no])
        print("Successfully Signed Up")
        time.sleep(2)
        clear_terminal()
        manager()