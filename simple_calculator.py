v1 = float(input("Enter The First Operand :\n"))
v2 = float(input("Enter The Second Operand :\n "))
ch = int(input("Choice Your Operation \n 1. Addition \n 2.subtraction \n 3.Multiplication \n 4.division \n "))
if ch == 1:
        print(v1,"+",v2,"=",v1+v2)
elif ch == 2:
        print(v1, "-", v2, "=", v1 - v2)
elif ch == 3:
        print(v1, "*",v2,"=",v1*v2)
elif ch == 4:
        print(v1,"/",v2,"=",v1/v2)
else:
        print("Invalid operation")