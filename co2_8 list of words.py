n=int(input("Enter the number of words in list:\n"))
w=[]
for i in range(n):
    a=input("Enter a word :")
    w.append(a)
l=len(w)
temp=a[0]
m=len(a[0])
for i in w :
    if len(i)>m:
        m=len(i)
        temp=i
print("The word with the longest length is:", temp," and length is ", m)

