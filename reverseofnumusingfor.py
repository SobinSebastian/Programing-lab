print("/// reverse of Number ///")
nb=int(input("Enter the Number:\n"))
t=str(nb)
rev=""
for i in range (0,len(t)) :
    rev=t[i]+rev
print("Reverse of",t,"is :",rev)

