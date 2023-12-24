import time
from terminal_clear import clear_terminal

    

def choose_user():
    while True:
        clear_terminal()
        print("***Welcome to GYM***\n")
        try:
            choice = int(input(f"1. A Customer?\n2. A Manager?\n"))
            if choice > 2:
                print("Pls choose only from given options")
                time.sleep(2)
                clear_terminal()
                continue
            clear_terminal()
            break
        except ValueError:
            print("Pls input integer for choice. Wait for 2 seconds")
            time.sleep(2)
            clear_terminal()
            
            
    if choice == 1:
        from customer_login import choose_customer
        choose_customer()
    elif choice == 2:
        pass