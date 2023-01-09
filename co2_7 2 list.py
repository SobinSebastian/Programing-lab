l=int(input("Enter the number of elements in list1 :"))
l1=[]
for i in range(l):
    v=int(input("Enter a integer value :\n\t"))
    l1.append(v)
n=int(input("Enter the number of elements in list2:"))
l2=[]
for i in range(n):
    u=int(input("Enter a integer value :\n\t"))
    l2.append(u)
if len(l1)==len(l2):
    print(" list are  same length\n")
else:
    print( "list are not same length\n")
s1=0
for i in l1:
    s1=s1+i
s2=0
for j in l2:
    s2=s2+j
if s1==s2:
    print("Sum of value of list are same\n")
else:
    print("Sum of value of list are not same\n")

a=set(l1)
b=set(l2)
print(" value occur in both list:",a.intersection(b))