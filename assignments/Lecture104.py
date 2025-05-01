class Customer:
    name = ""
    lastname = ""
    age = 0
    
    def addCart(self):
        print("Added to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "pakapron"
customer1.lastname = "lekwarakun"
customer1.addCart()

customer2 = Customer()
customer2.name = "woratep"
customer2.lastname = "lekwarakun"
customer2.addCart()

customer3 = Customer()
customer3.name = "sanom"
customer3.lastname = "lekwarakun"
customer3.addCart()

customer4 = Customer()
customer4.name = "Zandk"
customer4.lastname = "lekwarakun"
customer4.addCart()