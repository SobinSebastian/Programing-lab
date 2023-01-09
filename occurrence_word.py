print("\n /////////// Occurrences of each word in a text /////////// \n")
r=str(input("Enter your text :\n \t"))
l=r.split(" ")
t=set(l)
for j in t:
    c=0
    for i in l:
        if i==j:
            c=c+1
    print("Occurrences of",j,"=",c)