# program that repeatedly asks the user for a password until they enter "admin123".


correct_password = "admin123" # Correct password
password = ""    # Password that user will input

while password != correct_password: # != --> is not equal to
    password = input("Enter your password : ")  # = means equal to
    if password == correct_password: 
        print("Access graunted")   # Password == correct_password so access graunted.


    
