# given a list of student scores. Build a program that:

# Iterates through the list
# Prints "Fail" for scores below 50
# Prints "Pass" for scores 50 and above
# Skips further processing for failed scores using continue..


scores = [72, 45, 89, 30, 60]           # scores 

for i  in scores:
    if i < 50:                          # I less than scores
        print("Fail")                   # [72 > 50,  45 < 50 , 89 > 50, 30 < 50 , 60 > 50]
        continue
    print("Pass")
