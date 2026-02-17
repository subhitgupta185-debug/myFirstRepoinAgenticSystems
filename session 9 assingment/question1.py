# Read numbers.txt and load data

numbers_list = []

with open(r"C:\Users\subhi\Downloads\IIT Roorkie folder\Assignment folder\myFirstRepoinAgenticSystems\session 9 assingment\number.txt", "r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            number = int(clean_line)
            numbers_list.append(number)
print("data loaded")


