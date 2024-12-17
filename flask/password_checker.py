class PasswordChecker:
    '''
    Class to check the strength of passwords.
    '''
    def __init__(self, password):
        """
        Constructor method that takes a password and initializes instance variables.
        """
        self.password = password

    def get_password_rating(self):
        """
        Method that returns a string indicating the rating of the password.
        """
        # Check for uppercase letters, lowercase letters, numbers, and special characters
        has_upper = False
        has_lower = False
        has_number = False
        has_special = False
        for char in self.password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isnumeric():
                has_number = True
            elif not char.isalnum():
                has_special = True

        # Check against common passwords
        common_passwords = [
            "password", "123456", "qwerty", 
            "abc123", "letmein", "monkey", "password1", 
            "12345678", "admin", "welcome", "Password1!"
        ]
        if self.password in common_passwords:
            return "Very weak"

        # Check strength
        if len(self.password) < 8:
            return "Weak"
        elif len(self.password) < 12 and (not has_upper or not has_lower or not has_number):
            return "Moderate"
        elif len(self.password) < 12 and has_upper and has_lower and has_number:
            return "Strong"
        elif len(self.password) < 16 and has_upper and has_lower and has_number and has_special:
            return "Strong"
        elif len(self.password) >= 16:
            return "Very strong"
        else:
            return "Moderate"