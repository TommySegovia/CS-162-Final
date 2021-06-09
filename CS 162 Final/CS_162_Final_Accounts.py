# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:23:20 2021

@author: tommy
"""

class Account:
    def __init__(self, first_name = "none", last_name = "none"):
        '''Initializes the class Account's variables with it's default values '''
        self.first_name = first_name
        self.last_name = last_name
        


    def print_info(self):
        ''' Prints user first and last name along with the user's current balance to two decimal places '''
        print("")
        print("User name: {} {}" .format(self.first_name, self.last_name))
        print("Current balance: ${:.2f}\n" .format(self.balance))
        

        
    
        
