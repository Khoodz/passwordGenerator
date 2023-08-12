#Ahmad Khoder
#06/06/2023
#The Purpose of the program is to create a login system which will allow for employees to sign in, 
#and create accounts with the option of a random password generator


import time
import random
import string

#this is the password generator used to create random passwords
def generate_password(use_letters=True, use_digits=True, use_symbols=True):
    length = int(input("Enter the password length: "))  #choose password length

    characters = ""
    if use_letters: 
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ""
    for _ in range(length):
        random_character = random.choice(characters)
        password += random_character
    return password

#used to save accounts to accounts.txt file
def save_account_details(account_details):
    with open("accounts.txt", "a") as file:
        file.write(account_details + "\n")

#main menu functions for the program
def display_main_menu():
    print("Main Menu:")
    print("L. Log in")
    print("C. Create an account")
    print("V. View all usernames and passwords")
    print("E. Exit")

#This input is used to log into the system
def log_in():
    username = input("Enter your username: ")
    with open("accounts.txt", "r") as file:
        for line in file:
            account = [elem.strip() for elem in line.split(",")]
            if username == account[0]:
                password = input("Enter your password: ")
                if password == account[1]:
                    print("Login successful!")
                    return True
                else:
                    print("Invalid password.")
                    return False
    print("Invalid username.")
    return False

#This input is used as the create account function
def create_account():
    print("Create Account:")
    username = input("Enter a username: ")

    with open("accounts.txt", "r") as file:
        for line in file:
            account = [elem.strip() for elem in line.split(",")]
            if username == account[0]:
                print("Username already exists. Please choose a different username.")
                return

    choice = input("Enter 'Y' if you want to generate a password or 'N' to enter your own password: ")
    if choice.lower() == 'y':
        use_letters = input("Include letters? (Y/N): ").lower() == 'y'
        use_digits = input("Include digits? (Y/N): ").lower() == 'y'
        use_symbols = input("Include symbols? (Y/N): ").lower() == 'y'
        password = generate_password(use_letters=use_letters, use_digits=use_digits, use_symbols=use_symbols)  #password generator
        print("Generated Password:", password)
    else:
        password = input("Enter your password: ")

    account_details = username + "," + password
    print("Account created successfully!")
    save_account_details(account_details) #account saved to account.txt

#admin only view all login details
def view_all_usernames_and_passwords():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin1" and password == "admin1":
        with open("accounts.txt", "r") as file:
            for line in file:
                print(line.strip())
    else:
        print("Invalid credentials.")  #loop back to start

#while true loop for invalid entry, allows user to reinput option
while True:
    display_main_menu()
    choice = input("Enter your choice (L, C, V, or E): ")

    if choice.lower() == 'l':
        if log_in():
            
            break
    elif choice.lower() == 'c':
        create_account()
    elif choice.lower() == 'v':
        view_all_usernames_and_passwords()
    elif choice.lower() == 'e':
        print("Exiting program...")
        time.sleep(2)  # 2 seconds delay before quitting
        break
    else:
        print("Invalid choice. Please try again.")
