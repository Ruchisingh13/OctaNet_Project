# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:10:48 2024

@author: ruchi
"""

import time
from collections import deque

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"{amount} has been withdrawn from your account. New balance is {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} has been deposited to your account. New balance is {self.balance}"

    def get_balance(self):
        return self.balance

class Transaction:
    def __init__(self):
        self.history = deque(maxlen=10)  # Keeps last 10 transactions

    def add_transaction(self, transaction):
        self.history.appendleft(transaction)

    def get_history(self):
        return list(self.history)

class Transfer:
    def __init__(self, accounts):
        self.accounts = accounts

    def transfer(self, from_user, to_user, amount):
        if from_user not in self.accounts or to_user not in self.accounts:
            return "One of the accounts does not exist."
        if self.accounts[from_user].balance < amount:
            return "Insufficient funds for transfer."
        self.accounts[from_user].balance -= amount
        self.accounts[to_user].balance += amount
        return f"{amount} has been transferred from {from_user} to {to_user}."

class ATM:
    def __init__(self, users, accounts):
        self.users = users
        self.accounts = accounts
        self.transactions = {}
        for user in users:
            self.transactions[user.user_id] = Transaction()

    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin:
                return user
        return None

    def main_menu(self, user):
        while True:
            print("""
            1 == Transaction History
            2 == Withdraw
            3 == Deposit
            4 == Transfer
            5 == Quit
            """)
            
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid option.")
                continue
            
            if option == 1:
                history = self.transactions[user.user_id].get_history()
                if not history:
                    print("No transactions yet.")
                else:
                    for transaction in history:
                        print(transaction)

            elif option == 2:
                try:
                    amount = int(input("Please enter withdraw amount: "))
                    result = self.accounts[user.user_id].withdraw(amount)
                    print(result)
                    if "withdrawn" in result:
                        self.transactions[user.user_id].add_transaction(result)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            elif option == 3:
                try:
                    amount = int(input("Please enter deposit amount: "))
                    result = self.accounts[user.user_id].deposit(amount)
                    print(result)
                    if "deposited" in result:
                        self.transactions[user.user_id].add_transaction(result)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            elif option == 4:
                to_user = input("Enter the recipient user ID: ")
                try:
                    amount = int(input("Please enter transfer amount: "))
                    transfer = Transfer(self.accounts)
                    result = transfer.transfer(user.user_id, to_user, amount)
                    print(result)
                    if "transferred" in result:
                        self.transactions[user.user_id].add_transaction(result)
                        self.transactions[to_user].add_transaction(result)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            elif option == 5:
                print("Exiting... Thank you for using our service!")
                break
            
            else:
                print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # Create some users and accounts for testing
    users = [User('user1', 1111), User('user2', 2222)]
    accounts = {'user1': BankAccount(5000), 'user2': BankAccount(3000)}
    
    atm = ATM(users, accounts)
    
    print("Welcome to the ATM")
    user_id = input("Enter your user ID: ")
    try:
        pin = int(input("Enter your pin: "))
    except ValueError:
        print("Invalid pin. Please enter a numeric pin.")
        exit()
    
    authenticated_user = atm.authenticate_user(user_id, pin)
    
    if authenticated_user:
        print("Authentication successful!")
        atm.main_menu(authenticated_user)
    else:
        print("Authentication failed. Please check your user ID and pin.")
        

# Enter your user ID: user1

# Enter your pin: 1111