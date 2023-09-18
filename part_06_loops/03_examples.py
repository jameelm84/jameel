start=25
end=50
numbers = range(start,end)
for i in numbers:
    if i > 1 and i % 2 ==0:
        continue
    elif i > 1 :
     print(i)