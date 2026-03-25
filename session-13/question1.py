import pandas as pd

data = pd.read_csv("assingment.csv")
print(data)
#Loaded the csv data 


# Now using head() which shows the analysis of first 5(default) rows :

print("Head :")
head = data.head()
print(head)


# Now using trail to analyse last 5(Default) Rows :

print("Tail :")
tail = data.tail()
print(tail)


# Now structural info :
print("Structural info :")              # Shows the structural info like about str, int etc
structural = data.info()
print(structural)


# Summary of the data :

print("Summary :")
summary = data.describe()
print(summary)                      # Shows the summary of the data



subset_data = data[['Name', 'Marks']]
print(subset_data)