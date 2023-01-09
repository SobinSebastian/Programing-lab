i=int(input("Enter the Number:\n"))
k=2
c=0
while k<i:
    if i%k==0:
        c=c+1
    k=k+1
if c==0:
    print(i,"is A Prime Number")
elif c!=0:
    print(i,"is A non Prime Number")