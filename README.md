#A simple mini-bank

MinkBank is a Python-based console application designed to simulate basic banking operations. Users can register, log in, and manage their accounts with features such as balance inquiry, transfers, deposits, and withdrawals. The application ensures user information is securely stored in a local file for persistent access.

##Features
1. User Authentication

Login: Allows existing users to securely log in,
Register: New users can create an account with a username, password, and an initial balance of at least $1,000, and 
Password requirements include a minimum length of 8 characters, including uppercase, lowercase, digits, and special characters.

2. Banking Operations
Transfer: Transfer funds to another registered user,
Withdraw: Withdraw a specific amount from your account balance,
Deposit: Add funds to your account,
Balance Inquiry: View your current account balance,and
Update Information: Update your username or change your password.

3. Data Persistence
User information is stored in a text file (storing_data.txt) and 
User data includes:
   User ID,
   Username,
   Password,and
   Balance.

4. Error Handling and Validation
Input validations for username, password, and balance,
Prevents invalid or insufficient transactions,and
Ensures secure storage and retrieval of user data.


##How to Use
Prerequisites
Python must be higher than 3.8 installed on your machine.
Python Library
import re (for the special characters in order to validate the password or to ensure the passowrds )

##How to Run

For running the Application, 
Clone this repository:
( Ensur that you have installed Git App to use git command line or User interface)


  git clone https://github.com/your-username/minkbank.git, then,
  
  cd minkbank
  

Run the program:
python minkbank.py




Application Flow

Choose an Option:
  Press 1 to log in.
  Press 2 to register.
  Press any alphabetic character to exit.
  
  
Login:

  Enter your username and password to access your account.
  
  
Register:

  Provide a username, password, and initial balance to create an account.
  
Bank Menu Options:

   1: Transfer funds to another user.

   2: Withdraw money from your account.

   3: View your account balance.

   4: Update account details (username, password, or deposit funds).

   5: Exit the program.

##License:
This project is licensed under the MIT License.
Enjoy MinkBank! 😊


