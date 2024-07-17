import random             #to generate a random password
import string             #to generate a password with required datatypes

#defining the function for the process to generate password
def password_generator(password_length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password_create = '' .join(random.choice(chars) for i in range(password_length))
    print(f"The password with the length {password_length} is {password_create}")
    

password_length = int(input("Enter the length for the password:"))

#to check the given length is valid or not
if password_length >= 8:
    password_generator(password_length)
else:
    print("Invalid length!...")


