n = int(input('Enter a number : '))

for i in range(1, n*2):
    for j in range(i):
        print("#", end = " ")
    print()