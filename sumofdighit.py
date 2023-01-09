nb=int(input("Enter the Number:\n"))
t=nb
sum=0
while(nb!=0):
    s=nb%10
    sum=sum+s
    nb=nb//10
print("SUM Of Digits is :",sum)
