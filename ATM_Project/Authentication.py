from Database import Database

class Authentication():

    """ Authentication class for user authentication and PIN encryption """

    def __init__(self, user_id, pin):

        """ Initialize Authentication object with user ID and PIN """

        self.user_id = user_id
        self.pin = pin

    
    def encryption(self):

        """ Encrypt the user's PIN using a simple substitution cipher """

        result = ''
        # Dictionary for PIN encryption, mapping digits to letters
        encryption_dict = {i: chr(65 + i - 1) for i in range(1, 10)}

        for digit in self.pin:
            alphabet = encryption_dict[int(digit)]
            result += alphabet

        return result
    

    def is_authenticated(self):

        """ Authenticate the user """

        encrypted_pin = self.encryption()  # Encrypt the PIN
        valid = Database(self.user_id, encrypted_pin).user_verification()  # Verify user details

        if valid == True:
            return valid, encrypted_pin
        
    
    def new_pin(self, new_pin):

        """ Update user's PIN """

        encrypted_pin = ''
        encryption_dict = {i: chr(65 + i - 1) for i in range(1, 10)}
        valid, _ = self.is_authenticated()  # Check if user is authenticated

        if valid == True:
            for digit in new_pin:
                alphabet = encryption_dict[int(digit)]
                encrypted_pin += alphabet  # Encrypt the new PIN

        # Update PIN in the database
        Database(self.user_id, self.pin).update_pin(valid, encrypted_pin)
        
        return encrypted_pin
