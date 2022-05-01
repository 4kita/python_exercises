#my_first_tuple = (1, 2, 3)
#print(type(my_first_tuple))


from typing import Tuple


cardinal_tuple = ('first', 'second', 'third')

print(cardinal_tuple[1])

position1, position2, position3 = cardinal_tuple
print(position1)
print(position2)
print(position3)
my_Name = tuple("Frederick Lambert")
print("x" in my_Name)
newName = my_Name[0:17]
print(newName)