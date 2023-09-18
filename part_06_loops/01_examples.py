numbers =[12, 75, 34, 150, 180, 145, 525, 50]
print(type(numbers))
for x in numbers:
   if x > 500:
       break
   elif x > 150 :
        continue
   elif x % 5 == 0 :
      print(x)
