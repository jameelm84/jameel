enter_fisrt = int(input("first number =:"))
enter_second= int(input("second number =:"))
if enter_fisrt<enter_second :
  for i in range(enter_fisrt,enter_second+1):
      print(f"number {i} ; power of 2 ={i ** 2} ;power of 3 = {i **3 }   ")
if enter_fisrt>=enter_second :
    print("end")
