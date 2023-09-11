# print(range(5))
# print(type(range(5)))

range_iter =iter(range(5))
print(list(range_iter))

print(next(range_iter)) #  הבא בתור עד לסיום הרשימה לפי מה שהוגדר לה
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))

# for x in range(2,30,3):
#     print(x)
