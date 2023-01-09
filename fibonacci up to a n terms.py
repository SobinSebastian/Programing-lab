print("/// fibonacci series up to N terms  ///\n")
i=int(input("Enter N term to print fibonacci series:\n "))
a=0
b=1
print("fibonacci series \n")
if i==0:
    print("\n ", a)
elif i==1:
    print("\n",a,"\n",b)
else:
    print(a,"\n",b)
    for k in range(1,i):
        t=a+b
        a=b
        b=t
        if t<=i:
            print("\n",t)
        else:
            break
