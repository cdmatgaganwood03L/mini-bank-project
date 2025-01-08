import re

class Minkbank:
    def __init__(self):
        self.main_userinfo = self.load_user_info() or {}
        self.current_user_id: int = None

    def firstoption(self):
        print("\nPress 1 to Login or Press 2 to Register OR")
        print("Press any alphabetic character to exit.")
        option: str = input("\nPlease enter your choice: ")
        if option == '1':
            self.login()
        elif option == '2':
            self.register()
        elif option.isalpha():
            print("\nExiting....... \nThank you for banking with us!")
            exit()
        else:
            print("Your choice is not valid.\nPlease, try again.\n")
            return    

    def return_id(self, transfer_username):
        userinfo_length: int = len(self.main_userinfo)
        for i in range(1, userinfo_length + 1):
            if self.main_userinfo[i]["username"] == transfer_username:
                return i
        return None

    def bank_menu(self, login_ID):
        while True:
            menu_input: int = int(input("\nPlease, press 1 to transfer. \nPlease press 2 to withdraw. \nPlease, press 3 to view current balance. \nPlease, press 4 to update. \nPlease, press 5 to exit. \n_ _ _"))
            if menu_input == 1:
                transferto_username: str = input("Please, enter the username to transfer to: ")
                transfer_id: int = self.return_id(transferto_username)
                if transfer_id is None:
                    print("User is not found. Please, try again.")
                    continue
                transfer_amount: float = float(input("Enter amount to transfer: $"))
                if self.main_userinfo[self.current_user_id]["balance"] < transfer_amount:
                    print("Insufficient funds for your transfer.")
                    continue
                self.main_userinfo[self.current_user_id]["balance"] -= transfer_amount  
                self.main_userinfo[transfer_id]["balance"] += transfer_amount 
                print(f"${transfer_amount} transferred to {transferto_username} successfully.")
                print(f"The current balance is {self.main_userinfo[self.current_user_id]['balance']:.2f}")
                self.save_user_info(self.main_userinfo)

            elif menu_input == 2:
                withdraw_amount: float = float(input("Enter amount to withdraw: $"))
                if withdraw_amount > self.main_userinfo[self.current_user_id]["balance"]:
                    print("Insufficient funds!")
                else:
                    self.main_userinfo[self.current_user_id]["balance"] -= withdraw_amount
                    print(f"${withdraw_amount:.2f} withdrawn successfully!")
                    self.save_user_info(self.main_userinfo)

            elif menu_input == 3:
                Balance = self.main_userinfo[self.current_user_id]["balance"]
                print(f"\nYour current balance is: ${Balance:.2f}\n")

            elif menu_input == 4:
                update: int = int(input('\nPlease, press 1 to deposit your amount, \nPlease, press 2 to update your name, \nPlease, press 3 to change your password. \n _ _ _\n'))   
                while True:
                    if update == 1:
                        deposit_amount: float = float(input("Enter amount to deposit: $"))
                        self.main_userinfo[self.current_user_id]["balance"] += deposit_amount
                        print(f"${deposit_amount:.2f} deposited successfully!")
                        self.save_user_info(self.main_userinfo)
                        break
                    elif update == 2:
                        new_username: str = input("Enter new username: ")
                        while True:
                            if len(new_username) < 3 or len(new_username) > 20:
                                print("\nUsername must be between 3 and 20 characters.\n")
                            if not new_username.isalnum():
                                print("\nUsername must only contain alphanumeric characters.\n")
                                break
                            self.main_userinfo[self.current_user_id]["username"] = new_username
                            self.save_user_info(self.main_userinfo)
                            break
                        break
                    elif update == 3:
                        new_password: str = input("Enter new password: ")
                        while True:
                            if (len(new_password) < 8 or 
                                not any(char.isdigit() for char in new_password) or 
                                not any(char.isupper() for char in new_password) or 
                                not any(char.islower() for char in new_password) or 
                                not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in new_password)):
                                print("\nPassword must be at least 8 characters long.\nIt must include uppercase, lowercase, numbers, and special characters.\n")
                                break
                            self.main_userinfo[self.current_user_id]["password"] = new_password
                            print("Password changed successfully!")
                            self.save_user_info(self.main_userinfo)
                            break
                        break
                    else:
                        print("Your choice is not valid.")

            elif menu_input == 5:
                print("\nExiting.......\n")
                break
            else:
                print("Your choice is not valid.")

    def login(self):
        l_username: str = input("Please, enter your username: ")
        if len(l_username) < 3 or len(l_username) > 20:
            print("\nUsername must be between 3 and 20 characters.\n")
            return
        if not l_username.isalnum():
            print("\nUsername must only contain alphanumeric characters.\n")
            return
        
        l_password: str = input("Please, enter your password: ")
        if (len(l_password) < 8 or 
            not any(char.isdigit() for char in l_password) or 
            not any(char.isupper() for char in l_password) or 
            not any(char.islower() for char in l_password) or 
            not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in l_password)):
            print("\nPassword must be at least 8 characters long.\nIt must include uppercase, lowercase, numbers, and special characters.\n")
            return

        existing_user_id = self.check_existing_user(l_username, l_password)
        if existing_user_id:
            print("\n_____Login Successful!_____\n")
            self.current_user_id = existing_user_id
            self.bank_menu(existing_user_id)
        else:
            print("\nLogin failed. Please check your username and password.\n")

    def check_existing_user(self, username, password):
        user_check = len(self.main_userinfo)
        for i in range(1, user_check + 1): 
            if self.main_userinfo[i]["username"] == username and self.main_userinfo[i]["password"] == password:
                return i
        return None

    def register(self):
        r_username: str = input("\nPlease enter your username: ")
        if len(r_username) < 3 or len(r_username) > 20:
            print("\nUsername must be between 3 and 20 characters.\n")
            return
        if not r_username.isalnum():
            print("\nUsername must only contain alphanumeric characters.\n")
            return
        
        r_password1: str = input("Please enter your password: ")
        if (len(r_password1) < 8 or 
            not any(char.isdigit() for char in r_password1) or 
            not any(char.isupper() for char in r_password1) or 
            not any(char.islower() for char in r_password1) or 
            not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in r_password1)):
            print("\nPassword must be at least 8 characters long.\nIt must include uppercase, lowercase, numbers, and special characters.\n")
            return
        
        r_password2: str = input("Please confirm your password: ")
        initial_balance: int = int(input("Please enter your initial amount: $"))
        if initial_balance < 1000:
            print("\nYou must initialize your balance to at least $1,000.\n")
            return

        if r_password1 == r_password2:
            user_id: int = self.check_user_number()
            userinfo_form: dict = {user_id: {"username": r_username, "password": r_password2, "balance": initial_balance}}
            self.main_userinfo.update(userinfo_form)
            self.save_user_info(self.main_userinfo)
            print("\nYour information has been successfully registered.\n")
        else:
            print("\nPasswords do not match. Please try again.\n")

    def check_user_number(self):
        return len(self.main_userinfo) + 1
    
    def save_user_info(self, userinfo):
        try:
            with open("storing_data.txt", "w") as file:
                for user_id, info in userinfo.items():
                    print(f"Saving User ID: {user_id}, Username: {info['username']}, Balance: {info['balance']}")
                    file.write(f"User ID: {user_id}, Username: {info['username']}, Password: {info['password']}, Balance: {info['balance']}\n")
        except Exception as error:
            print("Your information could not be stored.")
            print(f'An error occurred while saving user info: {error}')
        finally:
            print("User information has been saved successfully.")

    def load_user_info(self):
        try:
            with open("storing_data.txt", "r") as file:
                read_data: list = file.readlines()
                userinfo = {}
                for line in read_data:
                    parts = line.strip().split(", ")
                    if len(parts) < 4:
                        continue
                    user_id = int(parts[0].split(": ")[1])
                    username = parts[1].split(": ")[1]
                    password = parts[2].split(": ")[1]
                    balance = float(parts[3].split(": ")[1])
                    userinfo[user_id] = {"username": username, "password": password, "balance": balance}
                    print(f"Loaded User ID: {user_id}, Username: {username}, Balance: {balance}")
                return userinfo
            
        except Exception as error:
            print(f"Error loading user info: {error}")
            return {}

if __name__ == "__main__":
    Bank = Minkbank()
    while True:
        Bank.firstoption()