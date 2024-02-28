from Authentication import Authentication
from Database import Database
from Transactions import Transaction
from datetime import date

class Account_management():

    """ Account_management class for managing user accounts and transactions """

    def __init__(self, user_id, pin):

        """ Initialize Account_management object with user ID and PIN """

        self.user_id = user_id
        self.pin = pin


    def user_authentication(self):

        """ Authenticate the user """

        valid, encrypted_pin = Authentication(self.user_id, self.pin).is_authenticated()
        return valid, encrypted_pin
    
    
    def get_account_details(self):

        """ Retrieve account details """ 
 
        valid, encrypted_pin = self.user_authentication()
        user_acc_dict = {}

        if valid == True:
            user_acc_dict = Database(self.user_id, encrypted_pin).retrive_query(bool_acc=True)

        return user_acc_dict


    def check_balance(self):

        """ Check account balance """

        valid, encrypted_pin = self.user_authentication()
        balance = 0

        if valid == True:
            balance = Database(self.user_id, encrypted_pin).retrive_query(bool_bal=True)

        return balance
    

    def deposit(self, amount):

        """ Deposit funds """

        valid, encrypted_pin = self.user_authentication()
        transaction = {'date': date.today(), 'amount': amount, 'Type':'credit'}  # store transaction record

        if valid == True:
            Transaction(self.user_id, encrypted_pin, transaction).process_transaction()    
        else:
            print('Transaction unsuccessful')

    
    def withdrawal(self, amount):

        """ Withdraw funds """

        valid, encrypted_pin = self.user_authentication()

        if amount < self.check_balance():  # amount not exceeding the account balance
            transaction = {'date': date.today(), 'amount': amount, 'Type':'debit'}  # store transaction record
            if valid == True:
                Transaction(self.user_id, encrypted_pin, transaction).process_transaction()    
            else:
                print('Transaction unsuccessful')


    def change_pin(self, new_pin):

        """ Change the user's PIN """

        encrypted_pin = Authentication(self.user_id, self.pin).new_pin(new_pin)  # call update pin function 
        return encrypted_pin
