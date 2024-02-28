from Database import Database


class Transaction():

    """ Transaction class for processing withdrawals and deposits """

    def __init__(self, user_id, pin, transaction):

        """ Initialize Transaction object with user ID, PIN, and transaction details """

        self.user_id = user_id
        self.pin = pin
        self.transaction = transaction


    def process_withdrawal(self):

        """ Process a withdrawal transaction """

        records = Database(self.user_id, self.pin).load_records()  # load records from database
        amount = self.transaction['amount']  # amount to withdraw

        for record in records:  # iterate over database
            if record['User_ID'] == self.user_id:  # check user id

                if 'Transactions' not in record:  # intialize transcation list if its not in the database
                    record['Transactions'] = []  

                record['Transactions'].append(self.transaction)  # append transaction
        
                record['Balance'] -= amount  # update balance
                print(f'Transcation successful! \n amount withdrawed!')
                Database(self.user_id, self.pin).save_records(records)  # update user record in database
                break        
        else: 
            print('Transaction unsuccessful!')



    def process_deposit(self):

        """ Process a deposit transaction """

        records = Database(self.user_id, self.pin).load_records()  # load records from database
        amount = self.transaction['amount']   # amount to deposit

        for record in records:
            if record['User_ID'] == self.user_id:  # check user id

                if 'Transactions' not in record:   # intialize transcation list if its not in the database
                    record['Transactions'] = []  

                record['Transactions'].append(self.transaction)  # append transaction
        
                record['Balance'] += amount
                print(f'Transcation successful! \n amount credited to your account!')  # update user record in database
                Database(self.user_id, self.pin).save_records(records)
                break        
        else: 
            print('Transaction unsuccessful!')


    def process_transaction(self):
            
            """ Process a transaction based on its type (debit or credit) """

            if self.transaction['Type'] == 'debit':
                self.process_withdrawal()
            elif self.transaction['Type'] == 'credit':
                self.process_deposit()
            else:
                print('something is wrong! check it')