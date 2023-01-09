print("/// fibonacci series ///\n")
j=int(input("Enter the limit to print fibonacci series:\n "))
a=0
b=1
i=1
print("fibonacci series \n")
if i==j:
    print("\n ", a)
elif i==j:
    print("\n",a,"\n",b)
else:
    print(a,"\n",b)
    for k in range(i):
        t=a+b
        a=b
        b=t
        if t<=j:
            print("\n",t)
            i=i+1