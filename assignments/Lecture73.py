systemMenu = {"fish":100,"pork":200,"bird":500}
menulist = []
while True:
    menuname = input("Please Enter Menu :")
    if (menuname.lower()== "exit"):
        break
    else:
        menulist.append([menuname,systemMenu[menuname]])


def showBill():
    total = 0
    print("-----My food -----")
    for i in range(len(menulist)):
        print(menulist[i][0],menulist[i][1])
        total += menulist[i][1]
    print("total : ",total)
print(menulist)
showBill()