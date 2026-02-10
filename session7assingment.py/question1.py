def user_name():
    name = input("Enter your name : ") 
    return name

def  greeting(name):
    greeting_sentence = "Hello! " + name
    return greeting_sentence

name = user_name()
greeting_sentence = greeting(name) 
print(greeting_sentence)