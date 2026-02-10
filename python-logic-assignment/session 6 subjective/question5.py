#  program that prints numbers from 1 to 10, but skips all even numbers.


for i in range(1, 11):
   if i % 2 == 0:
      continue
   print(i)