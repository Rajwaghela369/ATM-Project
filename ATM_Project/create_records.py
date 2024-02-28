import yaml

# Define ATM user records
atm_records = [
    {'User_ID': 'D17889', 'Pin': 'ABDC', 'Bank_Acc': 'DE1750090801', 'Bank_Name': 'Sparkasse', 'City': 'Berlin', 'First_Name': 'John', 'Last_Name':'Doe', 'Balance': 4000, 
     'Transactions': [{"date": "2024-02-13", "amount": 100, 'Type': 'debit'}, {"date": "2024-02-14", "amount": 50, 'Type': 'credit'}]},

     {'User_ID': 'D17880', 'Pin': 'GHDF', 'Bank_Acc': 'DE1750191801', 'Bank_Name': 'Sparkasse', 'City': 'Munich', 'First_Name': 'Marcus', 'Last_Name':'Rodriguez', 'Balance':7000, 
     'Transactions': [{"date": "2024-02-11", "amount": 100, 'Type': 'debit'}, {"date": "2024-01-14", "amount": 80, 'Type': 'credit'}]},

     {'User_ID': 'D17879', 'Pin': 'CDHG', 'Bank_Acc': 'DE1722291801', 'Bank_Name': 'Commerzbank', 'City': 'Stuttgart', 'First_Name': 'Julius', 'Last_Name':'Genevieve', 'Balance':10000, 
     'Transactions': []},

     {'User_ID': 'D17220', 'Pin': 'HCGH', 'Bank_Acc': 'DE1753191861', 'Bank_Name': 'Sparkasse', 'City': 'Brandenburg:', 'First_Name': 'Connor', 'Last_Name':'Davis', 'Balance':3000, 
     'Transactions': []},

     {'User_ID': 'D17451', 'Pin': 'CCDE', 'Bank_Acc': 'DE1750919199', 'Bank_Name': 'Commerzbank', 'City': 'Berlin:', 'First_Name': 'Adam', 'Last_Name':'Johnson', 'Balance':5000, 
     'Transactions': []},

     {'User_ID': 'D17331', 'Pin': 'FEFE', 'Bank_Acc': 'DE1723145868', 'Bank_Name': 'Deutsche Bank', 'City': 'Hamburg', 'First_Name': 'Sarah', 'Last_Name':'Smith', 'Balance':20000, 
     'Transactions': []},

     {'User_ID': 'D17199', 'Pin': 'DHEF', 'Bank_Acc': 'DE1750771871', 'Bank_Name': 'Deutsche Bank', 'City': 'Aachen', 'First_Name': 'Emily', 'Last_Name':'Martinez', 'Balance':9000, 
     'Transactions': []},

     {'User_ID': 'D17872', 'Pin': 'CDGE', 'Bank_Acc': 'DE1760891891', 'Bank_Name': 'Volksbank', 'City': 'Erlangen', 'First_Name': 'Emily', 'Last_Name':'Thompson', 'Balance':17155, 
     'Transactions': []},

     {'User_ID': 'D17222', 'Pin': 'EGHB', 'Bank_Acc': 'DE1750571851', 'Bank_Name': 'Sparkasse', 'City': 'Aachen', 'First_Name': 'Jasmine', 'Last_Name':'Patel', 'Balance':18555, 
     'Transactions': []},

     {'User_ID': 'D17575', 'Pin': 'BHBH', 'Bank_Acc': 'DE1750444821', 'Bank_Name': 'Commerzbank', 'City': 'Jena', 'First_Name': 'Olivia', 'Last_Name':'Kim', 'Balance':12000, 
     'Transactions': []},

     {'User_ID': 'D17464', 'Pin': 'CBCD', 'Bank_Acc': 'DE1740141231', 'Bank_Name': 'Volksbank', 'City': 'Erlangen', 'First_Name': 'Ethan', 'Last_Name':'Campbell', 'Balance':13000, 
     'Transactions': []},

     {'User_ID': 'D17785', 'Pin': 'BBDD', 'Bank_Acc': 'DE1756194221', 'Bank_Name': 'Deutsche Bank', 'City': 'Jena', 'First_Name': 'Caleb', 'Last_Name':'Lewis', 'Balance':25056, 
     'Transactions': []},
]

# Write ATM user records to YAML file
with open('Database.yaml', 'w') as file:
    yaml.dump(atm_records, file)
