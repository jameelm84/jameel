rever = [10,20,30,40,50] #solution 1 to print reversed list
# revl = reversed(rever)
# print(revl)
# listrev = list(revl)
# for x in listrev:
#     print(x)

# print(len(rever)) # solution 2 to print reversed list
#
# for num in rever[::-1]:
#     print(num)
jo=(len(rever))
print(jo)
for i in range(len(rever) - 1, -1, -1):
    print(rever[i])