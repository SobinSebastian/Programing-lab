#List comprehensions
l=int(input("Enter the number of elements:"))
li=[]
for i in range(l):
    v=int(input("Enter a integer value :\n\t"))
    li.append(v)
print("List of integers:\n",li)
nls= [n for n in li if n >=0]
print("List of Positive integers from List:\n",nls)