menulist = []
pricelist = []
total = 0
while True:
    menuname = input("Please Enter Menu :")
    if (menuname.lower()== "exit"):
        break
    else:
        menuprice = int(input("Price : "))
        menulist.append(menuname)
        pricelist.append(menuprice)
        total += menuprice


def showBill():
    print("-----My food -----")
    for i in range(len(menulist)):
        print(menulist[i],pricelist[i])
    print("total",total)

showBill()