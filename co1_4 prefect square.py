s=int(input("enter the 4 digit Starting range:\n"))
e=int(input("enter the 4 digit Ending range :\n"))
ls=[]
for i in range(s,e):
    if i%2==0:
        for j in range(1,i):
            if j*j==i:
                ls.append(i)
print (ls)
if len(ls)==0:
    print("")