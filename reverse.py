nb=int(input("Enter the Number:\n"))
t=nb
rev=0
while(nb!=0):
    s=nb%10
    rev=rev*10+s
    nb=nb//10
print("Reverse Of ",t," is :",rev)
