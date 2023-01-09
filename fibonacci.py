l=int(input("Enter the limit"))
f=n=0
s=1
print("Fibonacci series:\n",f,"\n",s)
while(n<l):
    t=f+s
    f=s
    s=t
    print(t,"\t")
    n=n+1