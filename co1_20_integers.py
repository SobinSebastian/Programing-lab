n=int(input("Enter the number of elements in list:\n"))
k=[]
for i in range(n):
    v=int(input("Enter a integer value:\n"))
    k.append(v)
print("the list is : \n ",k)
nl=[j for j in k if j%2==1]
print("new list after removing even numbers :\n",nl)