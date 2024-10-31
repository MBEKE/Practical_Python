#!/usr/bin/python3

tuple1 = (1, 9, 1, 6, 3, 4, 5, 3, 3, 4, 2, 8)
tuple2 = ()
for x in tuple1:
   if x not in tuple2:
      tuple2 += (x,)

print("Original tuple:", tuple1)
print("Unique numbers:", tuple2)
