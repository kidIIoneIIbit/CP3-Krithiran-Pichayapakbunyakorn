from currency_converter import CurrencyConverter

c = CurrencyConverter()

# ราคาเฉลี่ยของสินค้าต่อสกุลเงิน
item_price = {
    'USD': ('กาแฟ Starbucks', 5.00),
    'THB': ('ข้าวมันไก่', 45.00),
    'JPY': ('ราเมงชามเล็ก', 500.00),
    'EUR': ('ครัวซองต์', 2.50),
    'GBP': ('แซนด์วิช Tesco', 3.00),
    'CNY': ('ซาลาเปา', 3.50)
}

# รับค่าจากผู้ใช้
amount = float(input("💰 ป้อนจำนวนเงิน: "))
from_cur = input("จากสกุลเงิน (เช่น EUR): ").upper()
to_cur = input("เป็นสกุลเงิน (เช่น USD): ").upper()

try:
    rate = c.convert(1, from_cur, to_cur)
    result = c.convert(amount, from_cur, to_cur)

    print(f"\n📈 อัตราแลกเปลี่ยนล่าสุด: 1 {from_cur} ≈ {rate:.4f} {to_cur}")
    print(f"➡️ {amount} {from_cur} ≈ {result:.2f} {to_cur}")

    # แสดงของที่ซื้อได้จริง
    if to_cur in item_price:
        item_name, item_cost = item_price[to_cur]
        quantity = int(result // item_cost)
        print(f"\n🛍️ คุณสามารถซื้อ '{item_name}' ได้ประมาณ {quantity} ชิ้น (ราคาเฉลี่ย {item_cost} {to_cur}/ชิ้น)")
    else:
        print(f"\nℹ️ ยังไม่มีข้อมูลราคาสินค้าสำหรับสกุลเงิน {to_cur}")
except Exception as e:
    print("❌ เกิดข้อผิดพลาด:", e)
