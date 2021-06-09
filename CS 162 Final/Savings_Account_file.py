# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:56:03 2021

@author: tommy
"""

from CS_162_Final_Accounts import Account

class Savings(Account):
    def __init__(self, balance = 0, pin = 0000, interest = 0.03):
        Account.__init__(self)
        self.balance = balance
        self.interest = interest
        self.account_type = "Savings"