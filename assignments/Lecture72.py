menulist = []



while True:
    menuname = input("Please Enter Menu :")
    if (menuname.lower()== "exit"):
        break
    else:
        menuprice = int(input("Price : "))
        menulist.append([menuname,menuprice])


def showBill():
    total = 0
    print("-----My food -----")
    for i in range(len(menulist)):
        print(menulist[i])
        total += menulist[i][1]
    print("total : ",total)
print(menulist)
showBill()