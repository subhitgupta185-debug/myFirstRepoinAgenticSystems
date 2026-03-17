



marks = [25, 26, 15, 48, 58, 12, 17, 82]
#Index -  0   1  2   3    4   5   6   7

print("Full list :", marks)  # Displaying Full list : 

print("First 3 marks :", marks[:3])  # First three marks 
print("Last 3 marks :", marks[5:])   # Last three marks...

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest marks : ", highest)
print("lowest :", lowest)
print("Average of numbers :", average)