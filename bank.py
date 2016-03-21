"""
Author: Ken Lambert
Edited By: Leigh Stauffer
File: bank.py
Project 10

This module defines the SavingsAccount and Bank classes.
"""
import pickle
import random

class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02

    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __str__(self):
        result =  'Name:    ' + self._name + '\n' 
        result += 'PIN:     ' + self._pin + '\n' 
        result += 'Balance: ' + str(self._balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self._balance

    def getName(self):
        """Returns the current name."""
        return self._name

    def getPin(self):
        """Returns the current pin."""
        return self._pin

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        if amount < 0:
            return "Error: deposited amount must be greater than 0.00."
        else:
            self._balance += amount

    def withdraw(self, amount):
        """If the amount is valid, sunstract it
        from the balance and returns None;
        otherwise, returns an error message."""
        if amount > self._balance:
            return "Error: withdrawn amount must be less than current balance." 
        elif amount < 0:
            return "Error: withdrawn amount must be greater than 0.00."
        else:
            self._balance -= amount

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self._balance * SavingsAccount.RATE
        self._balance += interest
        return interest

class Bank:
    """This class represents a bank as a collection of savnings accounts.
    An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    # The state of the bank is a dictionary of accounts and
    # a file name.  If the file name is None, a file name
    # for the bank has not yet been established.

    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self._accounts = {}
        self._fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank."""
        return "\n".join(map(str, self._accounts.values()))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self._accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and
        and returns it, or None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self._accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank,
        or returns None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self._accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on
        all accounts."""
        total = 0
        for account in self._accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys."""
        keyList = []
        for account in self._accounts:
            keyList.append(account)
            keyList.sort()
        return keyList

    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return
        fileObj = open(self._fileName, 'wb')
        for account in self._accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

# Functions for testing
       
def createBank(numAccounts = 1):
    """Returns a new bank with the given number of 
    accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():
    """Test function for savings account."""
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number = 10, fileName = None):
    """Creates and prints a bank, either from
    the optional file name argument or from the optional
    number."""
    testAccount()
    if fileName:
        bank = Bank(fileName)
    else:
        bank = createBank(number)
    print(bank)

if __name__ == "__main__":
    main()

   
