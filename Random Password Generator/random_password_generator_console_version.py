import random
import string
import pyfiglet
import termcolor
import pyperclip
import time
import os

def clear_screen():
    os.system('cls') if os.name == "nt" else os.system('clear')

def loading_dots():
    for _ in range(4):
        print(termcolor.colored(".", "yellow"), end="")
        time.sleep(0.6)

def password_generator(length, has_upper, has_lower, has_digit, has_special):
    buffer = ''     

    if has_upper:
        buffer += string.ascii_uppercase
    if has_lower:
        buffer += string.ascii_lowercase
    if has_digit:
        buffer += string.digits
    if has_special:
        buffer += string.punctuation
    if not buffer:
        raise ValueError(termcolor.colored("At least one character type must be selected.", "yellow", attrs=["bold"]))
    
    password = ''.join([random.choice(buffer) for _ in range(length)])
    if has_upper:
        password = random.choice(string.ascii_uppercase) + password[1:]
    if has_lower:
        password = password[0] + random.choice(string.ascii_lowercase) + password[2:]
    if has_digit:
        password = password[0:2] + random.choice(string.digits) + password[3:]
    if has_special:
        password = password[0:3] + random.choice(string.punctuation) + password[4:] if (length > 4) else  password[0:3] + random.choice(string.punctuation) 
     
    shuffle_pass = list(password)
    random.shuffle(shuffle_pass)
    password = ''.join(shuffle_pass)   
    return password
            

def main():
    app_name = termcolor.colored(pyfiglet.figlet_format("RandomPass Generator", justify="center"), "green")
    msg_wel = termcolor.colored("WELCOME TO THE RANDOM PASSWORD GENERATOR", "yellow", attrs=["bold"])
    msg_start = termcolor.colored("Tap 'Enter' to launch the app", "yellow")
    msg_launch = termcolor.colored("Launching Password Generator", "yellow", attrs=["bold"])
    msg_ask = termcolor.colored("y/n", "red")
    msg_rec1 = termcolor.colored("Recommend : 8 characters or more", "magenta")
    msg_rec2 = termcolor.colored("Recommended", "magenta")
    msg_len = termcolor.colored("Length:", "blue")
    msg_chars = termcolor.colored("Characters", "blue")
    msg_paste = termcolor.colored("To paste! Use ", "blue")
    msg_crtl = termcolor.colored("CTRL + V", "red")
    msg_error_len = termcolor.colored("Password must be at least 4 characters long. Please try again!", "yellow")
    msg_error_number = termcolor.colored("Please enter a Number!", "yellow")
    msg_error_char = termcolor.colored("Please enter y or n", "yellow")
    msg_pas = termcolor.colored("P a s s w o r d  is  G e n e r a t e d", "blue")
    msg_y = termcolor.colored("Your Password: ", "blue")
    msg_reg = termcolor.colored("To regenerate press 'y' or 'Enter' to exit ", "black", attrs=["bold"])
    msg_gen = termcolor.colored("Press 'Enter' to generate your password ", "yellow", attrs=["bold"])
    msg_s_gen = termcolor.colored("Generating your password", "yellow", attrs=["bold"])
    msg_exit = termcolor.colored("Exiting", "yellow", attrs=["bold"])

    clear_screen()
    print(f"                                     {msg_wel}")
    input(msg_start)
    print(msg_launch, end="")
    loading_dots()
    while True:
        clear_screen()
        print(f"{app_name}")
        while True:
            length    = input(f"Enter password length ({msg_rec1}): ")
            try :
                length = int(length)
                if (length < 4):
                    print(f"{msg_error_len}")
                else:
                    break
                
            except ValueError:
                print(f"{msg_error_number}")
        
            
        while True:
            has_upper = input(f"Include uppercase letters ({msg_rec2})? ({msg_ask}): ").lower()
            try:
                if (has_upper != 'y' and has_upper != 'n'):
                    raise ValueError(f"{msg_error_char}")
                else :
                    has_upper = has_upper == 'y'
                    break
            except ValueError as er:
                print(er)
        while True:
            has_lower = input(f"Include lowercase letters ({msg_rec2})? ({msg_ask}): ").lower()
            try:
                if (has_lower != 'y' and has_lower != 'n'):
                    raise ValueError(f"{msg_error_char}")
                else:
                    has_lower = has_lower == 'y'
                    break
            except ValueError as er:
                print(er)

        while True:
            has_digit = input(f"Include digits ({msg_rec2})? ({msg_ask}): ").lower()
            try:
                if (has_digit != 'y' and has_digit != 'n'):
                    raise ValueError(f"{msg_error_char}")
                else:
                    has_digit = has_digit == 'y'
                    break
            except ValueError as er:
                print(er)

        while True:
            has_special = input(f"Include special characters ({msg_rec2})? ({msg_ask}): ").lower()
            try:
                if (has_special != 'y' and has_special != 'n'):
                    raise ValueError(f"{msg_error_char}")
                else:
                    has_special = has_special == 'y'
                    break
            except ValueError as er:
                print(er)        
   
        try:
            password = password_generator(length, has_upper, has_lower, has_digit, has_special)
            input(msg_gen)
            clear_screen()
            print(msg_s_gen, end="")
            loading_dots()
            pyperclip.copy(password)
            password = termcolor.colored(password, "yellow")
            msg_len_count = termcolor.colored(length, "red")
            clear_screen()
            print(f"""
                     ========================================
                    | {msg_pas} |
                    |----------------------------------------|
                    |   {msg_y} {password}  
                    |----------------------------------------|
                    |         {msg_len} {msg_len_count} {msg_chars}           |
                    |----------------------------------------|
                    |       {msg_paste} {msg_crtl}          |
                     ========================================         
                """)

            user_choice = input(msg_reg)
            if (user_choice.lower() != 'y'):
                print(msg_exit, end="")
                loading_dots()
                break

        except ValueError as error:
            print(error)
            input(termcolor.colored("Press 'Enter' to try again! ", "yellow", attrs=["bold"]))
        

if __name__ == "__main__":
    main()