salary = float(input("enter your salaray = "))
if salary >= 20000:
    print(f"your salary with tax is :" , (salary - (salary * 13/100)))
else:
    print (salary)