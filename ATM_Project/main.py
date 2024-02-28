import streamlit as st
from Account import Account_management
import pandas as pd

class ATM():

    """ ATM class to simulate ATM operations """

    def __init__(self):

        """ Initialize Streamlit page configuration """

        st.set_page_config(
            page_title = 'Welcome To Global ATM',
            layout = 'centered',
            initial_sidebar_state = 'collapsed'
        )

        
    def run(self):

        """ Run the ATM application """

        st.title("Welcome to Global ATM", anchor = False)

        current_page = self.get_current_page()
        
        # Determine which page to display based on the current state
        if current_page == 'login':
            self.Login()
        elif current_page == 'services':
            self.services()
        elif current_page == 'deposit':
            self.deposit()
        elif current_page == 'withdrawal':
            self.withdrawal()
        elif current_page == 'balance':
            self.balance()
        elif current_page == 'statement':
            self.statement()
        elif current_page == 'details':
            self.details()
        elif current_page == 'change pin':
            self.change_pin()


    def get_current_page(self):

        """ Get the current page from the session state """

        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'login'
        return st.session_state.current_page
    
    
    def Login(self):

        """ Login page """

        st.header('Login', anchor = False)

        self.user_id = st.text_input(label = 'User ID', placeholder ='Enter your User ID', max_chars = 12)
        self.pin = st.text_input(label = 'Pin', placeholder = 'Enter your Pin', max_chars = 4, type = 'password')
        self.login = st.button(label = 'Login', type = 'primary')

        # Check login credentials
        if self.login: 
            auth, _ = Account_management(user_id = self.user_id, pin = self.pin).user_authentication()
            if auth:
                st.session_state['user_id'] = self.user_id
                st.session_state['pin'] = self.pin
                st.session_state.current_page ='services'
            else:
                st.write('Invalid User ID or Pin')


    def services(self):

        """ Services page """

        st.header('Services', anchor = False)
        
        self.col1, self.col2 = st.columns(spec = 2)
        
        with self.col1:
            self.statement_button = st.button(label = 'Mini Statement', type = 'secondary')
            self.change_pin_button = st.button(label = 'Change Pin', type = 'secondary')
            self.details_button = st.button(label = 'Account Details', type = 'secondary')
            self.exit_button = st.button(label = 'Exit', type = 'primary')

        with self.col2:
            self.deposit_button = st.button(label = 'Deposit', type = 'secondary')
            self.withdrawal_button = st.button(label = 'Withdrawal', type = 'secondary')
            self.balance_button = st.button(label = 'Check Balance', type = 'secondary')

         # Determine which action to take based on button clicks
        if self.deposit_button:
            st.session_state.current_page = 'deposit'
        elif self.withdrawal_button:
            st.session_state.current_page = 'withdrawal'
        elif self.balance_button:
            st.session_state.current_page = 'balance'
        elif self.statement_button:
            st.session_state.current_page = 'statement'
        elif self.change_pin_button:
            st.session_state.current_page = 'change pin'
        elif self.details_button:
            st.session_state.current_page = 'details'
        elif self.exit_button:
            st.session_state.current_page = 'login'

      

    def deposit(self):

        """ Deposit money page """

        st.header('Deposit Money', anchor = False)

        self.input_amount = st.number_input(label = 'Amount', min_value = 0, max_value = 50000, )
        self.col1, self.col2 = st.columns(spec = 2)

        with self.col1: 
            self.cancel_button = st.button(label = 'Cancel', type = 'primary')
            if self.cancel_button:
                st.session_state.current_page = 'services'
        
        with self.col2:
            self.submit_button = st.button(label = 'Submit', type = 'secondary')
            if 0 > self.input_amount or self.input_amount > 50000:
                self.submit_button = False
                st.write('Please Enter amount between 0 to 50000')

        if self.submit_button:
            Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).deposit(self.input_amount)
            check_balance = Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).check_balance()
            st.markdown(f'##### Current Balance : {check_balance}')
            st.write('Transaction Successful!')


    def withdrawal(self):

        """ Withdraw money page """

        st.header('Withdraw Money', anchor = False)

        self.input_amount = st.number_input(label = 'Amount', min_value = 0, max_value = 50000)
        self.col1, self.col2 = st.columns(spec = 2)

        with self.col1: 
            self.cancel_button = st.button(label = 'Cancel', type = 'primary')
            if self.cancel_button:
                st.session_state.current_page = 'services'
        
        with self.col2:
            self.submit_button = st.button(label = 'Submit', type = 'secondary')
            if 0 > self.input_amount or self.input_amount > 50000:
                self.submit_button = False
                st.write('Please Enter amount between 0 to 50000')
        
        if self.submit_button:
            Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).withdrawal(self.input_amount)
            check_balance = Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).check_balance()
            st.markdown(f'##### Current Balance : {check_balance}')
            st.write('Transaction Successful!')
                
    
    def balance(self):

        """ Check balance page """

        st.header('Check Balance', anchor = False)

        self.acc_balance = Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).check_balance()

        st.markdown(f'#### Current Balance: {self.acc_balance}', unsafe_allow_html = True)

        self.back_button = st.button(label = 'Back', type = 'primary')
        if self.back_button:
            st.session_state.current_page = 'services'
        
    
    def statement(self):

        """ Statements page """

        st.header('Statments', anchor = False)

        self.transcation_statements = Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).get_account_details()

        if self.transcation_statements['Transactions'] == []:
            st.write('No Transactions available')
        else:
            df = pd.DataFrame(self.transcation_statements['Transactions'])
            st.dataframe(df)                  

        self.back_button = st.button(label = 'Back', type = 'primary')

        if self.back_button:
            st.session_state.current_page = 'services'

    
    def change_pin(self):

        """ Change PIN page """
  
        st.header('Change Pin', anchor = False)

        self.new_pin = st.text_input(label = 'New Pin', placeholder = 'Enter your New Pin', max_chars = 4, type = 'password')
        self.col1, self.col2 = st.columns(spec = 2)

        with self.col2:
            self.updated_button = st.button('Update', type ='secondary')
            if self.updated_button:    
                if self.new_pin == '':
                    st.write('Enter your New Pin')
                else:
                    Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).change_pin(new_pin = str(self.new_pin))
                    st.write('Pin Updated Successfully!')
                    st.session_state['pin'] = self.new_pin

        with self.col1:
            self.back_button = st.button(label = 'Back', type = 'primary')
            if self.back_button:
                st.session_state.current_page = 'services'

    
    def details(self):

        """ Account Details page """

        st.header('Account details', anchor = False)

        self.user_details = Account_management(user_id = st.session_state['user_id'], pin = st.session_state['pin']).get_account_details()
        self.iban = self.user_details['Bank_Acc']
        self.acc_balance = self.user_details['Balance']
        self.bank_name = self.user_details['Bank_Name']
        self.first_name = self.user_details['First_Name']
        self.last_name = self.user_details['Last_Name']
        self.city = self.user_details['City'] 

        st.markdown(f'#### Name: {self.first_name} {self.last_name}', unsafe_allow_html = True) 
        st.markdown(f'#### Bank Name: {self.bank_name}', unsafe_allow_html = True) 
        st.markdown(f'#### IBAN: {self.iban}', unsafe_allow_html = True) 
        st.markdown(f'#### Current Balance: {self.acc_balance}', unsafe_allow_html = True) 
        st.markdown(f'#### City: {self.city}', unsafe_allow_html = True) 

        self.back_button = st.button(label = 'Back', type = 'primary')
        if self.back_button:
            st.session_state.current_page = 'services'


if __name__ == "__main__":
    atm = ATM()
    atm.run()