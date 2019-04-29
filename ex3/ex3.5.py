# Python 3 version

# Code for reading in the date */
date = input("Please enter date (DD/MM/YYYY): ")
d, m, y = date.split('/')
d = int(d)
m = int(m)
y = int(y)

#isLeapDay = (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))
#isMouthOneOrTwo = (m == 1 or m == 2)
#if isMouthOneOrTwo and isLeapDay:
#    d = d - 2
#elif isMouthOneOrTwo and not isLeapDay:
#    d = d - 1
#elif isMouthOneOrTwo:
#    m = m + 12

if m == 1:
    m = 13
    y = y - 1
elif m == 2:
    m = 14
    y = y - 1

z = 1 + d + (m * 2) + (3 * (m + 1) // 5) + y + y//4 - y//100 + y//400

z %= 7

days = ["Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"]

print(days[z]+'day')
