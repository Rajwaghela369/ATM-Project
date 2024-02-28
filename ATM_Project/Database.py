import yaml

class Database():

    """ Database class for managing user records stored in a YAML file """
    
    def __init__(self, user_id, pin) -> None:

        """ Initialize the Database object with user ID and PIN """

        self.user_id = user_id
        self.pin = pin

    
    def load_records(self):
        
        """ Load user records """

        global path
        path = 'Database.yaml' 

        with open(path, 'r') as file:   # read the database
            return yaml.safe_load(file)
        
        
    def save_records(self, records):

        """ Save updated user records """

        with open(path, 'w') as file:   # write the database
            yaml.dump(records, file)

        
    def user_verification(self):

        """ Verify user details """

        records = self.load_records()
        valid = False  # bool

        for record in records:  # iterate over database
            if (record['User_ID'] == self.user_id) & (record['Pin']== self.pin):  # check user id and pin to verify
                valid = True

        return valid
    
 
    def update_pin(self, valid, new_pin):

        """ Update user's PIN """

        records = self.load_records()

        if valid == True:
            for record in records:  # iterate over database
                if record['User_ID'] == self.user_id:  # check user id
                    record['Pin'] = new_pin  # change pin
                    break        
            self.save_records(records)  # save the updated pin
        else:
            print('Incorrect login!')
            
    
    def retrive_query(self, bool_bal = False, bool_acc = False):

        """ Retrieve account details or balance """

        records = self.load_records() 
        acc_details = {}

        for record in records:   # iterate over database
            if record['User_ID'] == self.user_id:  # check user id
                acc_details = record  # retrive account details
            else:
                pass
        
        # check if user retriving account balance or account details
        if bool_acc == True:  # wants account details
            return acc_details
        elif bool_bal == True:  # wants account balance
            return acc_details['Balance']  # retrive account balance
        else:
            print('Please select a service')
