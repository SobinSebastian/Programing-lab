print("character frequency in a string :\n")
s=str(input("Enter the string :\n \t"))
r=set(s)
for i in r:
    c=0
    for j in s:
        if i==j and j!=" ":
            c=c+1

    print(i,c)