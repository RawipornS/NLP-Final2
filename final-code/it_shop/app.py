from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# รายการสินค้าพร้อมราคา
products = {
    "โทรศัพท์": 5000,
    "คอมพิวเตอร์": 20000,
    "หูฟัง": 1000,
    "กล้องถ่ายรูป": 15000
}

# ฟังก์ชันแนะนำสินค้าแบบสุ่ม
def recommend_product():
    return random.choice(list(products.keys()))

# ฟังก์ชันสำหรับร้านขายของ
def shop_bot(message):
    message = message.lower()

    # การต้อนรับ
    if "สวัสดี" in message or "hello" in message:
        return "ยินดีต้อนรับสู่ร้านของเรา! เรามี โทรศัพท์, คอมพิวเตอร์, หูฟัง, และกล้องถ่ายรูป คุณสนใจสินค้าอะไร?"

    # การแนะนำสินค้าสุ่ม
    if "แนะนำสินค้า" in message:
        product = recommend_product()
        price = products[product]  # ดึงราคา
        return f"ผมขอแนะนำ {product} ซึ่งเป็นสินค้าที่ได้รับความนิยมมาก! ราคาอยู่ที่ {price} บาท"

    # แสดงรายการสินค้า
    if "มีอะไรขายบ้าง" in message or "สินค้า" in message:
        return "เรามีสินค้าต่อไปนี้: โทรศัพท์, คอมพิวเตอร์, หูฟัง, และกล้องถ่ายรูป คุณสนใจสินค้าอะไร?"

    # ตรวจสอบราคาสินค้า
    for product, price in products.items():
        if product.lower() in message:  # ตรวจสอบว่าชื่อสินค้าปรากฏในข้อความหรือไม่
            return f"{product} มีราคาอยู่ที่ {price} บาท"

    # การตอบสนองต่อคำสั่งซื้อ
    if "สั่งซื้อ" in message:
        return "ขอบคุณที่สั่งซื้อ! กรุณาระบุที่อยู่สำหรับจัดส่ง และชำระเงินผ่านช่องทางที่คุณสะดวก."

    elif "ขอบคุณ" in message:
        return "ยินดีครับ ขอบคุณที่มาอุดหนุน หากต้องการซื้อสินค้าเพิ่มเติมสามารถสอบถามได้เลยครับ!"

    else:
        return "ผมไม่เข้าใจคำสั่งของคุณ ลองถามเกี่ยวกับสินค้าหรือพิมพ์ 'แนะนำสินค้า' เพื่อรับคำแนะนำ"

# Route สำหรับหน้าเว็บหลัก
@app.route("/")
def home():
    return render_template("index.html")

# Route สำหรับรับข้อความจากผู้ใช้
@app.route("/get")
def get_response():
    userText = request.args.get('msg')
    response = shop_bot(userText)
    return jsonify(response)

if __name__ == "__main__":
    app.run()
