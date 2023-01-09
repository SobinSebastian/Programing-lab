k=int(input("Enter the number of rows:\n"))
for i in range(1,k+1):
    for j in range(1,i+1):
        print(j*i,end=" ")
    print("\n")