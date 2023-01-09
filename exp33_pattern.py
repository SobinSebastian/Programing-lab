i=int(input("Enter the Number of rows"))
j=1
while j<=i:
    k=i
    while k>=j:
        print("*",end="")
        k=k-1
    print("")
    j=j+1