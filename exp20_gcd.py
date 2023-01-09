k=int(input("Enter the frist Number : \n"))
j=int(input("Enter the second Number :\n"))
i=1
if(k>j):
    s=j 
else:
    s=k
while i<=s:
    if ((k%i==0) and (j%i==0)):
        g=i
    i=i+1
print("GCD of",k," and ",j," is  :",g)