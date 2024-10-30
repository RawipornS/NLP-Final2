from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Template ที่ใช้ในการตอบกลับข้อความ
bot_template = "BOT : {0}"

# กำหนดคำถามและคำตอบที่ต้องการ
responses = {
    "ประเทศที่ใหญ่ที่สุดในโลกคืออะไร": "ประเทศรัสเซียเป็นประเทศที่ใหญ่ที่สุดในโลก",
    "สัตว์ที่เร็วที่สุดในโลกคืออะไร": "เสือชีตาห์เป็นสัตว์ที่เร็วที่สุดในโลก",
    "อาหารประจำชาติของประเทศไทยคืออะไร": "อาหารประจำชาติของไทยคือผัดไทย",
    "คุณชอบอาหารอะไร": "ฉันเป็นบอท ไม่มีความสามารถในการกินอาหาร แต่ฉันได้ยินว่าผัดไทยอร่อยมาก!",
    "default": "ขอโทษค่ะ ฉันไม่เข้าใจคำถามนี้"
}

# ฟังก์ชันสำหรับตรวจสอบคำถามและตอบกลับ
def respond(message):
    # ตรวจสอบว่าข้อความที่ได้รับอยู่ใน responses หรือไม่
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = responses["default"]
    return bot_message

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]  # รับข้อความจากผู้ใช้
    response = respond(user_input)  # ส่งคำถามไปที่ฟังก์ชันเพื่อหาคำตอบ
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
