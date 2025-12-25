n = int(input("what day of chirstmas? "))

def each(num):
    if n >= num:
        giftNum = ((n + 1) - num) * num
    else:
        giftNum = 0
    return giftNum

if n > 12:
    print("past christmas!")
elif n < 0:
    print("before christmas!")
else:
    gifts = 0.5 * (((n*(n+1))/2) + ((n*(n+1)*(2*n+1))/6))
    print("Gifts:", gifts, "\n")

print("Partridges in pear trees:", each(1))
print("Turtles Doves:", each(2))
print("French Hens:", each(3))
print("Calling Birds:", each(4))
print("Golden Rings:", each(5))
print("Geese o' laying:", each(6))
print("Swans a-swimming:", each(7))
print("Maids of milking:", each(8))
print("ladies dancing:", each(9))
print("Lords a-leaping:", each(10))
print("Pipers Piping:", each(11))
print("Drummers Drumming:", each(12))