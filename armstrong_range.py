print("Armstrong Numbers with in a Range \n")
l=int(input("Enter the lower range : \n  "))#take input from user
u=int(input("Enter the upper range : \n  "))
print("Armstrong numbers between ",l," and ",u,"\n")
while l<u+1:
    t=l
    n=l
    rev=0
    #code finding sum of cube of each digit
    while(n!=0):
        s=n%10
        rev=rev+s*s*s
        n=n//10
    if rev==t:
        print("\t",t)
    l=l+1