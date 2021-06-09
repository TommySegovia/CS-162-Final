# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:21:50 2021

@author: tommy
"""


from Savings_Account_file import Savings
from Checking_Account_file import Checking
import matplotlib.pyplot as plt
import numpy as np
from random import randint
        
    
        
def admin_pie_plot():
    account_name_list = []
    random_color_list = []
    value_list = []
    for account in account_dict:
        value_list.append(account_dict[account])
        name_split = account.split()
        account_name_list.append(name_split[0] + " " + name_split[1] + str("\n${:,.2f}" .format((account_dict[account]))) + "({})" .format(name_split[3]))
        random_color_list.append("#" + str(randint(100000, 999999))) 
                                 
    y = value_list
        
        
    mylabels = account_name_list
    plt.title('Bank Portfolio Distribution')
    mycolors = random_color_list
    plt.pie(y, labels = mylabels, colors= mycolors, autopct='%1.1f%%')
    
    plt.show() 


        


def partition(user_ids, i, k):
    pivot = user_ids[k]
    index = i - 1
    for j in range(i,k):
        if user_ids[j] <= pivot:
            index += 1
            user_ids[index], user_ids[j] = user_ids[j], user_ids[index]
    user_ids[index + 1], user_ids[k] = user_ids[k], user_ids[index + 1]
    return index + 1
 
def quicksort(user_ids, i, k):
    if i < k:
        piv = partition(user_ids, i, k)
        quicksort(user_ids, i, piv - 1)
        quicksort(user_ids, piv + 1, k)
        
def sort_accounts():
    unsorted_list = []
    for account in account_dict:
        name_split = account.split()
        unsorted_list.append(str("\n${:,.2f}" .format(account_dict[account])) + " "  + name_split[0] + " " + name_split[1])
        
    quicksort(unsorted_list, 0, len(unsorted_list) - 1)
    unsorted_list.reverse()
    for i in unsorted_list:
        print(i)
    print("")


    
def print_menu():
    ''' Prints the prompt for the user to choose between searching an account, creating an account, printing all accounts as an admin or quitting'''
    print("a - Account search")
    print("c - Create Account\n")
    print("r - Remove Account (ADMIN)")
    print("s - Sorted Accounts (ADMIN)")
    print("l - List accounts (ADMIN)")
    print("p - Plot Accounts Portfolio (ADMIN)\n")
    print("q - Quit\n")
    print("Choose an option:\n")
        
def options_menu():
    ''' Prints the menu for the user choices inside their account, between deposit, withdraw, printing account info, and going back to the previous menu'''
    print("d - Deposit")
    print("w - Withdraw")
    print("t - Transfer")
    print("p - Print user info\n")
    print("r - Remove Account")
    print("b - Back")
    print("Choose an option:\n")
    
def admin_print():
    ''' Iterates through account_dict and prints each account by number, name, pin, and balance to two decmials'''
    print("")
    counter = 1
    for account in account_dict:
        account_list = account.split(" ") #Creates a list by spliting the key from the account_dict
        print("Account #{}\n Name: {} {}\n Pin: {}\n ${:,.2f}\n Account Type: {}\n" .format(counter, account_list[0], account_list[1], account_list[2], account_dict[account], account_list[3]))
        counter += 1   
        
def withdraw():
    ''' Prompts user for a withdrawal amount, withdraws from account if balance allows'''
    withdraw_amount = int(input("Enter withdrawal amount:\n"))
    print("")
    if withdraw_amount < account_dict[search_login]: 
        account_dict[search_login] -= withdraw_amount
        print("${:,.2f} Successfully Withdrawn\n" .format(withdraw_amount))
    else:
        print("Cannot withdraw: ${:,.2f}" .format(withdraw_amount)) #Assures that the user will not withdraw more than they have
        print("Account balance: ${:,.2f}\n" .format(account_dict[search_login]))
        
def deposit():
    ''' Prompts user for a deposit amount and deposits the amount into the user balance'''
    deposit_amount = int(input("Enter deposit amount:\n"))
    print("")
    account_dict[search_login] += deposit_amount
    print("${:,.2f} Successfully Deposited\n" .format(deposit_amount))
    
def transfer():
    transfer_value = float(input("Enter a value to transfer to savings\n"))
    account_dict[search_login] -= transfer_value
    account_dict[transfer_search] += transfer_value
    print("Successfully transfered ${:,.2f}" .format(transfer_value))
    
def remove_account():
    user_input = ""
    while user_input != "b":
        remove_search = search_first + " " + search_last + " " + search_pin + " " + account_type
        if remove_search in account_dict:    
            account_dict.pop(remove_search)
            print("Account Successfully removed")
            user_input = "b"
        else:
            print("Account not found")
            print("Enter r to try searching again")
            print("Enter b to go back")
            user_input = input()
def admin_remove_account():
    user_input = ""
    while (user_input != "b"):
        user_input = ""             
        search_first = input("Enter account first name:\n")                         
        search_last = input("Enter account last name:\n")                                
        search_pin = input("Enter account pin:\n")
        account_type = input("Enter account type(Savings / Checking)\n")
        
        
        remove_search = search_first + " " + search_last + " " + search_pin + " " + account_type
        if remove_search in account_dict:
            account_dict.pop(remove_search)
            user_input = "b"
        else:
            print("Account not found")
            print("press r to try searching again")
            print("Press b to go back")
            user_input = input()
        
    
class input_Error(Exception):
    def __init__(self, value):
        self.value = value
    
# class
    
try:
    user_input = ""
    account_dict = {} #Creates dictionary for accounts
    
     
    print("")
    print("Welcome User\n")
    
    while user_input != "q":
        print_menu()
        user_input = input("")
        
        try:
            
            search_first = ""
            search_last = ""
            search_pin = "0000"
            search_login = "N/a"
            
            if user_input == "c": #input for creating an account
                user_confirm = "n"
                pin = ""
                checking_or_savings = (input("Enter Checking or Savings\n"))
                if checking_or_savings == "Checking":            
                    new_account = Checking() #Creates a new ccount
                elif checking_or_savings == "Savings":
                    new_account = Savings()
                while new_account.first_name != "q" and new_account.last_name != "q" and pin != "q" and user_confirm != "y":
                    
                    first_name = input("Enter account first name:\n")
                    last_name = input("Enter account last name:\n")
                    pin = "0000"
                    verify_pin = "1111"
                    while pin != verify_pin: #verifies that the pin is correctly entered twice
                        pin = input("Create a four didgit pin:\n")
                        verify_pin = input("Enter pin again to confirm:\n")
                        print("")
                        if pin != verify_pin:
                            print("Pin does not match")
                            print("Please try again\n")
                    balance = int(input("Deposit amount:\n"))
                    print("")
                    
                    new_account.first_name = first_name
                    new_account.last_name = last_name
                    new_account.pin = pin
                    new_account.balance = balance
                    
                    new_account.print_info()
                    user_confirm = input("Confirm? (y / n)\n")
                    
                    
                        
                    
                print("")
                
                user_login = new_account.first_name + " " + new_account.last_name + " " + pin + " " + new_account.account_type
                #creates the user login info to be stored in the dictionary
                
                account_dict[user_login] = new_account.balance
                #stores the user login info with the value of the account balance
                    
                
                
                
            
            
                
            elif user_input == "a": #input for searching an account
                
                while (user_input != "b"):
                    user_input == ""             
                    search_first = input("Enter account first name:\n")                         
                    search_last = input("Enter account last name:\n")                                
                    search_pin = input("Enter account pin:\n")
                    account_type = input("Enter account type(Savings / Checking)\n")
                    
                            
                    print("")
                    solo_print = search_login.split(" ") #Creates a list by spliting the key from the account_dict
                    search_login = search_first + " " + search_last + " " + search_pin + " " + account_type
                    
                    
                    if search_login in account_dict:  
                        
                        print("Account: {} {}" .format(search_first, search_last))
                        print("Current Balance: ${:,.2f}" .format(account_dict[search_login]))
                        print("Account type: {}" .format(account_type))
                        print("Welcome User\n")
                                      
                        while user_input != "b":
                            options_menu() #Calls the options menu function for user choice on deposit and withdrawal  
                            user_input = input()
                            if user_input == "d":
                                deposit()
                            elif user_input == "w":
                                withdraw()
                            elif user_input == "r":
                                remove_account()
                                user_input = "b"
                            elif user_input == "t":
                                print("")
                                print("--Choose the account you wish to tranfer to--\n")
                                while (user_input != "b"):
                                    try:
                                        user_input == ""             
                                        search_first = input("Enter account first name:\n")                         
                                        search_last = input("Enter account last name:\n")                                
                                        search_pin = input("Enter account pin:\n")
                                        account_type = input("Enter account type(Savings / Checking)\n")
                                        
                                                
                                        print("")
                                        solo_print = search_login.split(" ") #Creates a list by spliting the key from the account_dict
                                        transfer_search = search_first + " " + search_last + " " + search_pin + " " + account_type
                                        
                                        
                                        if search_login in account_dict:
                                            transfer()
                                            user_input = "b"
                                        else:
                                            print("Account not found\n")
                                            print("Enter t to try again")
                                            print("Enter b to go back")
                                            user_input = input()
                                    except KeyError:
                                        print("\n----- ERROR -----\n----- Account not found -----")
                                user_input = ""
                                    
                            elif user_input == "p":
                                                        
                                search_login_split = search_login.split()
                                print("Name: {} {}\n Pin: {}\n ${:,.2f}\n Account Type: {}" .format(search_login_split[0], search_login_split[1], search_login_split[2], account_dict[search_login], search_login_split[3]))
                            elif user_input == "b":
                                pass
                            else:
                                raise input_Error("\n----- ERROR -----\n----- Incorrect input -----\n")
                                
                    else: #prompts the user to retry entering the login info or quit
                        print("Invalid login information:\n")
                        print("To try searching again enter: a")
                        print("To go back enter: b\n")
                        user_input = input()
                        
                            
                        
            elif user_input == "l":
                admin_print()
            
            elif user_input == "r":
                admin_remove_account()
                
            elif user_input == "p":
                admin_pie_plot()
                
            elif user_input == "s":
                sort_accounts()
            
            elif user_input == "q":
                print("Quitting...")
            
            else:
                raise input_Error("\n----- ERROR -----\n----- Incorrect input -----\n")
                
        except input_Error as ex:
            print(ex)
            
        except ValueError:
            print("\n----- ERROR -----\n----- Please enter a number ------\n")
            
        except NameError:
            print("\n----- ERROR -----\n----- Please enter Checking or Savings -----\n")
except input_Error as ex:
    print(ex)

        
        
  