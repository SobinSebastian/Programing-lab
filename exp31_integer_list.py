g=[1,2,3,4,5,6,7,8,9]
odd=g.copy()
i=0
print("Original list :",g,"\n")
while i<len(g):
    j = g[i]
    if(j%2==0):
       odd.remove(j)
    i=i+1
print("List after removing even numbers :\n",odd)