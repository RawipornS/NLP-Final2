from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# เทมเพลตสำหรับการตอบกลับของบอท
bot_template = "BOT : {0}"

# กำหนดการตอบกลับที่เป็นไปได้ที่เกี่ยวข้องกับคณะ IT ในมหาวิทยาลัย KMUTNB
responses = {
    'greeting': [
        "Hello, can I help you with anything?",  # ตอบกลับเมื่อผู้ใช้ทักทาย
        "Hi there! What would you like to know?",  # ตอบกลับพร้อมข้อเสนอให้ช่วยเหลือ
        "Greetings! How can I assist you today?",  # ตอบกลับอีกแบบ
    ],

    'statement': [
        'That sounds interesting!',  # ตอบกลับเมื่อผู้ใช้พูดอะไรที่น่าสนใจ
        'Tell me more about it!',  # เชิญชวนให้ผู้ใช้เล่ารายละเอียดเพิ่มเติม
        'What do you think about that?',  # ถามความคิดเห็นของผู้ใช้
        'Wow, that’s cool!',  # ตอบกลับเมื่อผู้ใช้พูดถึงสิ่งที่น่าสนใจ
        'That’s fascinating!',  # ตอบกลับเมื่อผู้ใช้พูดถึงสิ่งที่น่าทึ่ง
        'Oh, I see!'  # ตอบกลับเมื่อเข้าใจสิ่งที่ผู้ใช้พูด
    ],

    # ข้อมูลทั่วไปในคณะ 
    'question': [
        "The FITM Faculty organizes studies in Prachinburi Province.",  # ข้อมูลเกี่ยวกับการศึกษาที่คณะ FITM
        "There are 4 departments in total.",  # จำนวนภาควิชาทั้งหมด
        "Graduates from the IT faculty are well-prepared for careers in software development, IT management, and data analysis."  # ความพร้อมของผู้สำเร็จการศึกษา
    ],

    # ข้อมูลภาควิชา
    'department': [
        "Department of Information Technology (IT)\n",  # ภาควิชาคอมพิวเตอร์
        "Department of Industrial Management (IM)\n",  # ภาควิชาการจัดการอุตสาหกรรม
        "Department of Construction Design and Management (CDM)\n",  # ภาควิชาการออกแบบและบริหารงานก่อสร้าง
        "Department of Agricultural Engineering for Industry (AEI)"  # ภาควิชาวิศวกรรมเกษตรเพื่ออุตสาหกรรม
    ],

    # รายละเอียดสาขา
    'majors': {
        "IT": "Bachelor of Science Program in Information Technology, Information and Network Engineering.",  # สาขาวิชา IT
        "IM": "Bachelor of Engineering Program in Industrial Engineering and Management, Industrial Science Program in Industrial Management.",  # สาขาวิชา IM
        "CDM": "Bachelor of Science Program in Construction Design and Management.",  # สาขาวิชา CDM
        "AEI": "Bachelor of Engineering Program in Agricultural and Food Engineering, Technology and Production Processes."  # สาขาวิชา AEI
    },

    'default': [
        "I'm sorry, I don't have information on that.",  # ขอโทษที่ไม่มีข้อมูลในเรื่องนั้น
        "Could you please ask another question about the IT faculty?"  # โปรดถามคำถามอื่นเกี่ยวกับคณะ IT
    ],

    # คำถามกำหนดไว้ล่วงหน้า
    'custom_questions': {
        "what's your name?": "My name is Bot.",  # การตอบสำหรับคำถามเกี่ยวกับชื่อ
        "what's today's weather?": "The weather is cloudy."  # การตอบสำหรับคำถามเกี่ยวกับสภาพอากาศ
    }
}

# ฟังก์ชันเพื่อสร้างการตอบกลับตามข้อมูลที่ผู้ใช้ป้อน
def get_response(message):
    message = message.strip().lower()  # แปลงข้อความให้เป็นตัวพิมพ์เล็กและลบช่องว่าง

    # ตรวจสอบคำทักทายจากผู้ใช้
    if "hi" in message or "hello" in message or "hey" in message:
        return random.choice(responses['greeting'])  # ตอบกลับด้วยข้อความทักทาย

    if message == "bye":
        return "Goodbye! The chat has ended."  # ตอบเมื่อผู้ใช้พิมพ์ "bye"

    # ตรวจสอบคำถามที่กำหนดไว้ล่วงหน้า
    for question, answer in responses['custom_questions'].items():
        if question in message:
            return answer  # ตอบคำถามที่กำหนดไว้ล่วงหน้า

    # ตรวจสอบคำถามเกี่ยวกับภาควิชา
    if "what departments are in the faculty?" in message:
        return ', '.join(responses['department'])  # ตอบรายการภาควิชา

    # ตรวจสอบคำถามเกี่ยวกับสาขาวิชา
    if "can i have information about the majors in" in message:
        if "it" in message:  # ถ้าถามเกี่ยวกับภาควิชา IT
            return responses['majors']["IT"]  # ตอบสาขาวิชาของ IT
        elif "im" in message:  # ถ้าถามเกี่ยวกับภาควิชา IM
            return responses['majors']["IM"]  # ตอบสาขาวิชาของ IM
        elif "cdm" in message:  # ถ้าถามเกี่ยวกับภาควิชา CDM
            return responses['majors']["CDM"]  # ตอบสาขาวิชาของ CDM
        elif "aei" in message:  # ถ้าถามเกี่ยวกับภาควิชา AEI
            return responses['majors']["AEI"]  # ตอบสาขาวิชาของ AEI
        else:
            return "Please specify the department to get information about the majors."  # แจ้งให้ระบุภาควิชา

    elif message.endswith('?'):
        # ตอบคำถามทั่วไป
        return random.choice(responses.get("question", responses["default"]))  # ตรวจสอบการตอบคำถามทั่วไป

    elif message:
        # ตอบข้อความทั่วไป
        return random.choice(responses.get("statement", responses["default"]))  # ตรวจสอบการตอบข้อความทั่วไป

    return "Please type something so I can respond."  # แจ้งให้พิมพ์ข้อความ

# กำหนดเส้นทางสำหรับหน้าเว็บหลัก
@app.route("/")
def index():
    return render_template("index.html")  # เรนเดอร์หน้าเว็บหลัก

# กำหนดเส้นทางสำหรับการตอบกลับของบอท
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]  # รับข้อความจากผู้ใช้
    response = get_response(user_input)  # เรียกใช้ฟังก์ชัน get_response
    return jsonify(response)  # ส่งคำตอบกลับในรูปแบบ JSON

# รันแอปพลิเคชัน Flask
if __name__ == "__main__":
    app.run(debug=True)  # รันเซิร์ฟเวอร์ Flask
