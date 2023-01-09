s=str(input("Enter a string:\n"))
if len(s)>2:
    if s[-3:]=='ing':
        s=s+'ly'
    else:
        s=s+'ing'
print(s)
