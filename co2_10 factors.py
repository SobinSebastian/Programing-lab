n=int(input("Enter the Number:\n"))
print("Factors of ",n)
for i in range(1,n+1):
    if n%i==0:
        print(i)