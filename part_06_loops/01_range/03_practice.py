#print(list(range(25,172,8))) # start,end,step
#practice 23
a = 9
b = 15

for i in range(a,b+1):
    if i % 3 == 0 and  i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0   :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else:
        print(i)



