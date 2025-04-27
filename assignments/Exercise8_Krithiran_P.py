username = input("Username: ")
password = input("Password: ")
if username == "kid" and password == "lelouch":
    print("Welcome to kid shop!!!")
    products = {
        "1": ["เสื้อยืด", 250],
        "2": ["กางเกงยีนส์", 800],
        "3": ["รองเท้าผ้าใบ", 1500],
        "4": ["หมวกแก๊ป", 150]
    }
    print("รายการสินค้า:")
    for code, (name, price) in products.items():
        print(f"{code}. {name} - {price} บาท")
    print("กรุณาเลือกสินค้า")
    one = int(input("รับเสื้อยืดจำนวน: "))
    two = int(input("รับกางเกงยีนส์จำนวน: "))
    three = int(input("รับรองเท้าผ้าใบจำนวน: "))
    four = int(input("รับหมวกแก๊ปจำนวน: "))
    
    total = (one*250)+(two*800)+(three*1500)+(four*150)
    print(f"ราคาทั้งหมด {total} บาท")