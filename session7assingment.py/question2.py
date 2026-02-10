def add_numbers(a,b):
    add = a + b
    return add

first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

add = add_numbers(first_number, second_number)
result = "Sum is :",  add
print(result)