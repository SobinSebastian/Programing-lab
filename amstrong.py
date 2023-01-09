n=int(input("Enter the Number:\n"))
t=n
rev=0
while(n!=0):
    s=n%10
    rev=rev+s*s*s
    n=n//10
if rev==t:
    print(t,"Is Armstorng Number")
else:
    print(t,"Is not a Armstorng Number")