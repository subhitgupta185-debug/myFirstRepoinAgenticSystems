amount_balance = int(input("Enter your balance :")) # Int = integer, input = This operator is used for taking the input from the user.
withdrawl = int(input("Enter your withdrwal amount :")) # User enter the withdrawl amount
verification_status = True  # If verification == True, Transaction successfull.
balance_remaining = amount_balance - withdrawl  # For finding remaining balance

if amount_balance > withdrawl and verification_status == True:
    print("Withdrawl successful") # amount balance > withdrawl so withdrawl successfull
else:
    print("Transaction denied") # amount balance < withdrawl so withdrawl denied.

print(balance_remaining) # Balance Remaining....