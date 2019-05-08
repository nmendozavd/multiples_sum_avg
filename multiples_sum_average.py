"""
#print all odds from 1 to 1000
for i in range(1, 101, 2): print i

#print all multiples of 5, from 5 to 1,000,000.
for i in range(0, 1000000, 5): print(i)

#Print sum of all values in list a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a)

#Print average of all values in list a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
"""


# Multiples
for odd in range(0, 1000):
    if odd % 2 == 1:
        print odd

for fives in range (5, 1000000):
    if fives % 5 == 0:
        print fives


# Sum List
a = [1, 2, 5, 10, 255, 3]
print sum(a)


# Average List
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
