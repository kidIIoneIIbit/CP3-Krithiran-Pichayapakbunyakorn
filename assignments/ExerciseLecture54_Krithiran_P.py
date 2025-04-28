def login():
    usernameInput = input("Username: ")
    PasswordInput = input("Password: ")
    if usernameInput == "admin" and PasswordInput == "1234":
        return True
    else:
        False
def showmenu():
    print("Done !!!")
    print("----iShop----")
    print("1.vat calculater")
    print("2.Price Calculater")
def menuselect():
    userSelected = int(input(">>"))
    return userSelected
def vatcalcalate(totalprice):
    vat = 7
    result = totalprice + (totalprice*vat/100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price :"))
    price2 = int(input("Second Product Price :"))
    return vatcalcalate(price1+price2)
    

login()
showmenu()
if menuselect()==1:
    num = int(input())
    print(vatcalcalate(num))
else:
    print(priceCalculate)