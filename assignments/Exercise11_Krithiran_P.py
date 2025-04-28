number = int(input("number: "))
var = number-1
for i in range(1,number*2,2):
        print(" "*var,end="")
        print("*"*(i))
        var -= 1