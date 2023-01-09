l=int(input("Enter the number of elements:"))
name=[]
for i in range(l):
    v=input("Enter a name :\n\t")
    name.append(v)
o=str(name)
c=0
for k in o:
    if k=="a":
        c=c+1
print(c,"times a is occur in list")