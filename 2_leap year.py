s=int (input("Enter the year :\n\t"))
e=int(input("Enter the End year:\n\t"))
print("Leap years between",s,"and",e ,":")
for i in range(s,e+1):
    if i%4==0:
        print(i)