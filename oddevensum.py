limit=int(input("Enter  The Limit :\n"))
i=1
s=0
t=0
while i <= limit:
    if i % 2 == 0:
        s = s+i
    elif i%2==1:
        t=t+i
    i=i+1
print("Sum of Even Numbers is: \n",s)
print("Sum of Odd Numbers is:",t)
