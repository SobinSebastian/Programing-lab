k=int(input("Enter the number the elements :\n"))
l=[]
for i in range(k):
    j=int(input("Enter the Number:\n"))
    l.append(j)
print(l)
sq=[n * n for n in l]
print("list of Squares:")
print(sq)