print("/// Armstorng Number /// \n")
n=int(input("Enter the Number:\n"))
t=str(n)
rev=0
for i in t:
    v=int(i)
    rev = rev + v * v * v

if rev==n:
    print(n,"Is Armstorng Number")
else:
    print(n,"Is not a Armstorng Number")