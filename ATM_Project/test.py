import unittest as ut
from Account import Account_management
from datetime import date

class TestAccountManagement(ut.TestCase):

    """ Test ATM Functionalities """
    
    def test_user_authentication(self):

        """ Test user authentication """

        ## Test case for user 1
        valid_1, encrypted_pin_1 = Account_management(user_id = 'D17889', pin = "1245").user_authentication()
        ut.TestCase.assertEqual(self, first = valid_1, second = True)
        ut.TestCase.assertEqual(self, first = "ABDE", second = encrypted_pin_1, msg = 'verified account')
        print('Test case user_authentication: user 1 = PASSED')

        ## Test case for user 2
        valid_2, encrypted_pin_2 = Account_management(user_id = 'D17880', pin = "4455").user_authentication()
        ut.TestCase.assertEqual(self, first = valid_2, second = True)
        ut.TestCase.assertEqual(self, first = "DDEE", second = encrypted_pin_2, msg = 'verified account')
        print('Test case user_authentication: user 2 = PASSED')

    
    def test_get_account_details(self):

        """ Test get account details """

        ## Test case for user 1
        account_1 = Account_management(user_id = 'D17889', pin = "1245").get_account_details()
        balance_1 = 4278
        first_name_1 = 'John'
        last_name_1 = 'Doe'
        bank_name_1 = 'Sparkasse'
        city_1 = 'Berlin'
        iban_1 = 'DE1750090801'

        ut.TestCase.assertEqual(self, first = balance_1, second = account_1['Balance'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = first_name_1, second = account_1['First_Name'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = last_name_1, second = account_1['Last_Name'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = bank_name_1, second = account_1['Bank_Name'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = city_1, second = account_1['City'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = iban_1, second = account_1['Bank_Acc'], msg = 'verified account')
        print('Test case get_account_details: user 1 = PASSED')

        ## Test case for user 2
        account_2 = Account_management(user_id = 'D17331', pin = "6565").get_account_details()
        balance_2 = 20000
        first_name_2 = 'Sarah'
        last_name_2 = 'Smith'
        bank_name_2 = 'Deutsche Bank'
        city_2 = 'Hamburg'
        iban_2 = 'DE1723145868'

        ut.TestCase.assertEqual(self, first = balance_2, second = account_2['Balance'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = first_name_2, second = account_2['First_Name'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = last_name_2, second = account_2['Last_Name'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = bank_name_2, second = account_2['Bank_Name'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = city_2, second = account_2['City'], msg = 'verified account')
        ut.TestCase.assertEqual(self, first = iban_2, second = account_2['Bank_Acc'], msg = 'verified account')
        print('Test case get_account_details: user 2 = PASSED')


    
    def test_check_balance(self):

        """ Test check balance """

        ## Test case for user 1
        balance_1 = Account_management(user_id = 'D17889', pin = "1245").check_balance()
        ut.TestCase.assertEqual(self, first = 4278, second = balance_1, msg = 'verified account')
        print('Test case check_balance: user 1 = PASSED')

        ## Test case for user 2
        balance_2 = Account_management(user_id = 'D17880', pin = "4455").check_balance()
        ut.TestCase.assertEqual(self, first = 8895, second = balance_2, msg = 'verified account')
        print('Test case check_balance: user 2 = PASSED')

    

    def test_deposit(self):

        """ Test deposit """

        ## Test case for user 1
        Account_management(user_id = 'D17785', pin = "2244").deposit(amount = 400)
        updated_balance_1 = Account_management(user_id = 'D17785', pin = "2244").check_balance()
        ut.TestCase.assertEqual(self, first = 8800 + 400, second = updated_balance_1, msg = 'verified account')
        print('Test case deposit: user 1 = PASSED')

        ## Test case for user 2
        Account_management(user_id = 'D17464', pin = "3234").deposit(amount = 300)
        updated_balance_2 = Account_management(user_id = 'D17464', pin = "3234").check_balance()
        ut.TestCase.assertEqual(self, first = 15400 + 300, second = updated_balance_2, msg = 'verified account')
        print('Test case deposit: user 2 = PASSED')

    def test_withdrawal(self):

        """ Test withdrawal """

        ## Test case for user 1
        Account_management(user_id = 'D17575', pin = "4321").withdrawal(amount = 40)
        updated_balance_1 = Account_management(user_id = 'D17575', pin = "4321").check_balance()
        ut.TestCase.assertEqual(self, first = 11160 - 40, second = updated_balance_1, msg = 'verified account')
        print('Test case withdrawal: user 1 = PASSED')

        ## Test case for user 2
        Account_management(user_id = 'D17222', pin = "7769").withdrawal(amount = 30)
        updated_balance_2 = Account_management(user_id = 'D17222', pin = "7769").check_balance()
        ut.TestCase.assertEqual(self, first = 20425 - 30, second = updated_balance_2, msg = 'verified account')
        print('Test case withdrawal: user 2 = PASSED')
 
    
    def test_change_pin(self):

        """ Test change PIN """

        ## Test case for user 1
        pin_1 = Account_management(user_id = 'D17879', pin = "7657").change_pin(new_pin = '7788')
        ut.TestCase.assertEqual(self, first = 'GGHH', second = pin_1, msg = 'verified account')
        print('Test case change_pin: user 1 = PASSED')

        ## Test case for user 2
        pin_2 = Account_management(user_id = 'D17451', pin = "7879").change_pin(new_pin = '8899')
        ut.TestCase.assertEqual(self, first = 'HHII', second = pin_2, msg = 'verified account')
        print('Test case change_pin: user 2 = PASSED')


if __name__ == '__main__':
    ut.main()