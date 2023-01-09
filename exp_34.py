n = int(input('Enter number of rows : '))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
k=1
while k<=(n-1):
    l=n-1
    while l>=k:
        print("*", end="")
        l= l-1
    print()
    k= k + 1