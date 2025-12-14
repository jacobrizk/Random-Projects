#Project Euler Q0
#Sum of all odd square numbers for the first 223000 numbers you square.

squareNums = []

for numbers in range(1, 223000+1):
    if numbers % 2 != 0:
        square = numbers**2
        squareNums.append(square)

odds = sum(squareNums)

print(odds)