s=str(input("Enter the String: \n \t"))
l=s[0]
for i in s:
    if i==l:
        s=l+s[1:].replace(l,'$')
print(s)