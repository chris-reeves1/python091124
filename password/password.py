import sqlite3

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

# SQLite Database Setup
DATABASE = "password_history.db"

def setup_database():
    """
    Function to set up the SQLite database and the required table.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT NOT NULL,
                rating TEXT NOT NULL
            )
        """)
        conn.commit()

def add_password_to_db(password, rating):
    """
    Function to add a password and its rating to the database.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (password, rating) VALUES (?, ?)", (password, rating))
        conn.commit()

def get_ratings_for_password(password):
    """
    Function to fetch all ratings for a given password from the database.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT rating FROM history WHERE password = ?", (password,))
        return [row[0] for row in cursor.fetchall()]

def display_history():
    """
    Function to display the full password history from the database.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password, rating FROM history")
        rows = cursor.fetchall()
        print("History:")
        for row in rows:
            print(f"Password: {row[0]} - Rating: {row[1]}")

# Main Program
setup_database()

while True:
    password_check = input("Enter a password: ")

    # Check if the password already exists in the database
    ratings = get_ratings_for_password(password_check)

    if ratings:
        print(f"Password rating (from history): {ratings[-1]}")
    else:
        # Calculate the password rating
        checker = PasswordChecker(password_check)
        rating = checker.get_password_rating()

        # Store in the database
        add_password_to_db(password_check, rating)
        print(f"Password rating: {rating}")

    # Display history
    display_history()

    # Check if user wants to continue
    answer = input("Enter another password? (y/n): ")
    if answer.lower() != "y":
        break
