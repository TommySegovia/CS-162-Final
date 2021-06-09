# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:56:17 2021

@author: tommy
"""

from CS_162_Final_Accounts import Account

class Checking(Account):
    def __init__(self, balance = 0, pin = 0000):
        Account.__init__(self)
        self.balance = balance
        self.account_type = "Checking"