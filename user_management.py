# import hashlib

# class Database:

#     user_list = []

#     opens_time = 0

#     def __init__(self):

#         Database.user_list += 1

#         print(Database.user_list)

#     @staticmethod
#     def password_hashing(password):
        
#         hashed_password = hashlib.sha256(password.encode())
#         return hashed_password

#     @staticmethod
#     def add_user(data):
#         Database.user_list.append(data)
#         print("User registered successfully.")
        


# class RegisterUser(Database):

#     def __init__(self, username, email, password):

#         self.username = username
#         self.email = email
#         self.password = password

#     def register_me(self):

#         database = Database.user_list

#         for user in database:

#             if user.get("username") in user:

#                 return f"Username already exist, please use another username."

            
#             elif user.get("username") not in user:

#                 hashed_password = Database.password_hashing(self.password)

#                 print(hashed_password, "password")

#                 data = {
#                     "username": self.username,
#                     "email": self.email,
#                     "password": hashed_password
#                 }

#                 Database.add_user(data)

#             else:

#                 print("Something went wrong.")



# username = input("Enter Your Username: ")

# email = input("Enter Your Email: ")

# password = input("Enter Your Password: ")


# user = RegisterUser(username, email, password)

# user.register_me()





# Corrected Code

import hashlib

class Database:

    user_list = []  # This will store the list of user data dictionaries.

    @staticmethod
    def password_hashing(password):
        # Hash the password using SHA-256 and return the hexadecimal digest
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    @staticmethod
    def add_user(data):
        Database.user_list.append(data)
        print("User registered successfully.")


class RegisterUser:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def register_me(self):
        database = Database.user_list

        # Check if the username already exists
        for user in database:
            if user.get("username") == self.username:
                return "Username already exists, please use another username."

        # Hash the password and add the user
        hashed_password = Database.password_hashing(self.password)
        data = {
            "username": self.username,
            "email": self.email,
            "password": hashed_password
        }
        Database.add_user(data)
        return "User registered successfully."


# Take user input
username = input("Enter Your Username: ")
email = input("Enter Your Email: ")
password = input("Enter Your Password: ")

# Create a new user and register them
user = RegisterUser(username, email, password)
result = user.register_me()
print(result)

# Optional: Print all users in the database
print("All registered users:")
for u in Database.user_list:
    print(u)


                

