nb=int(input("Enter the Number:\n"))
t=nb
rev=0
while(nb!=0):
    s=nb%10
    rev=rev*10+s
    nb=nb//10
if t==rev:
    print(t,"Is Palindrome")
else:
    print(t,"Is Not Palindrome")
