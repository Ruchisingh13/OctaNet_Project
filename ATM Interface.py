# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:10:48 2024

@author: ruchi
"""

class Atm:
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        while True:
            user_input = input("""
            Hello, how would you like to proceed?
            1. Enter 1 to create Pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to Check balance
            5. Enter 5 to Exit
            """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4": 
                self.check_balance()
            elif user_input == "5":
                print("Exiting... Thank you for using our service!")
                break
            else:
                print("Invalid option, please try again.")
        
    def create_pin(self):
        self.pin = input("Enter your Pin: ")
        print("Pin set successfully")
        
    def deposit(self):
        temp = input("Enter your Pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Deposit successful")
        else:
            print("Invalid Pin")
        
    def withdraw(self):
        temp = input("Enter your Pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")
             
    def check_balance(self):
        temp = input("Enter your Pin: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid Pin")

# Create an instance of the Atm class to run the ATM menu
atm = Atm()
