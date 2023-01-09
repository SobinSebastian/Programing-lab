print("/// Palindrome Number ///")
nb=int(input("Enter the Number:\n"))
t=str(nb)
rev=""
for i in range (0,len(t)) :
    rev=t[i]+rev
if t==rev:
    print(t,"Is Palindrome")
else:
    print(t,"Is Not a Palindrome")
