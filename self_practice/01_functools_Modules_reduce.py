#import functools
#from functools import * # מייבא את כל המודול
from functools import reduce as re# מייבא את הפונקציה REDUCE ונותנים שם חלופי אליאס RE


my_list = [1, 2, 3, 4, 5, 6, 7]
total = re(lambda x,y : x+y, my_list) # reduce sum all elements into list
multiplication = re(lambda x,y : x*y, my_list) # reduce multiplication all elements into list

print(total)
print(multiplication)

