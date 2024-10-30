# นำเข้าไลบรารีที่จำเป็นสำหรับการสร้างแอปพลิเคชัน Flask, การวิเคราะห์ความรู้สึก และการจัดการข้อความ
from flask import Flask, request, jsonify, render_template
import random
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# สร้างแอปพลิเคชัน Flask
app = Flask(__name__)

# ดาวน์โหลดไฟล์ข้อมูลสำหรับการวิเคราะห์ความรู้สึกของ NLTK
nltk.download('vader_lexicon')

# สร้างวัตถุสำหรับการวิเคราะห์ความรู้สึกโดยใช้เครื่องมือ VADER (SentimentIntensityAnalyzer)
sid = SentimentIntensityAnalyzer()

# สร้างชุดของกฎสำหรับการตอบสนองของแชทบอท
# โดยใช้การจับคู่รูปแบบข้อความ เช่นคำถามและคำตอบที่เป็นไปได้
rules = {
    'do you think (.*)': [
        'If {0}? Absolutely.',  # ตัวอย่างคำตอบที่ 1 สำหรับคำถามที่ตรงกับรูปแบบนี้
        'No chance.'  # ตัวอย่างคำตอบที่ 2 สำหรับคำถามที่ตรงกับรูปแบบนี้
    ],
    'do you remember (.*)': [
        'Did you think I would forget {0}?',  # ตัวอย่างคำตอบที่ 1
        "Why haven't you been able to forget {0}?",  # ตัวอย่างคำตอบที่ 2
        'What about {0}?',  # ตัวอย่างคำตอบที่ 3
        'Yes .. and?'  # ตัวอย่างคำตอบที่ 4
    ],
    'I want (.*)': [
        'What would it mean if you got {0}?',  # คำถามสะท้อนถึงความต้องการของผู้ใช้
        'Why do you want {0}?',  # คำถามสะท้อนเหตุผล
        "What's stopping you from getting {0}?"  # สอบถามสิ่งที่ขัดขวางความต้องการ
    ],
    'if (.*)': [
        "Do you really think it's likely that {0}?",  # สอบถามถึงความน่าจะเป็นของสถานการณ์
        'Do you wish that {0}?',  # สอบถามความต้องการ
        'What do you think about {0}?',  # ถามความคิดเห็น
        'Really--if {0}!'  # ตอบด้วยความแปลกใจ
    ]
}

# ฟังก์ชันสำหรับจับคู่ข้อความผู้ใช้กับกฎที่ตั้งไว้
def match_rule(rules, message):
    # ค่าเริ่มต้นสำหรับการตอบสนองและข้อความที่จะนำไปใส่ในคำตอบ
    response, phrase = "default", None
    # วนลูปเพื่อหากฎที่ตรงกับข้อความผู้ใช้
    for pattern, responses in rules.items():
        # ใช้ regex ในการตรวจสอบว่าข้อความตรงกับรูปแบบใดในกฎหรือไม่
        match = re.match(pattern, message)
        if match:
            # เลือกการตอบสนองแบบสุ่มจากตัวเลือกที่ตรงกับกฎนั้น ๆ
            response = random.choice(responses)
            if "{0}" in response:
                # ถ้าในคำตอบมีตัวแปร {0} แสดงว่าต้องแทนที่ด้วยส่วนหนึ่งของข้อความที่จับคู่ได้
                phrase = match.group(1)
    return response, phrase  # ส่งกลับคำตอบและข้อความที่จะนำไปใช้แทนที่

# ฟังก์ชันสำหรับแทนที่สรรพนามในข้อความ เพื่อให้คำตอบดูเป็นธรรมชาติขึ้น
def replace_pronouns(message):
    # แปลงข้อความเป็นตัวพิมพ์เล็กเพื่อความสะดวกในการประมวลผล
    message = message.lower()
    # แทนที่คำว่า 'me' ด้วย 'you' เพื่อปรับเปลี่ยนคำตอบให้เหมาะสม
    if 'me' in message:
        message = message.replace('me', 'you')
    # แทนที่ 'my' ด้วย 'your'
    if 'my' in message:
        message = message.replace('my', 'your')
    # แทนที่ 'your' ด้วย 'my'
    if 'your' in message:
        message = message.replace('your', 'my')
    # แทนที่ 'you' ด้วย 'me'
    if 'you' in message:
        message = message.replace('you', 'me')
    return message  # ส่งกลับข้อความที่ถูกแทนที่

# ฟังก์ชันสำหรับสร้างคำตอบจากข้อความผู้ใช้
def respond(message):
    # ตรวจสอบว่าข้อความผู้ใช้ตรงกับกฎใดใน rules
    response, phrase = match_rule(rules, message)
    # ถ้าคำตอบที่ได้มีตัวแปร {0} และมีข้อความที่ต้องแทนที่
    if '{0}' in response and phrase:
        # เรียกใช้ฟังก์ชัน replace_pronouns เพื่อแทนที่สรรพนามในข้อความ
        phrase = replace_pronouns(phrase)
        # ใส่ข้อความแทนที่ลงในตำแหน่ง {0} ในคำตอบ
        response = response.format(phrase)
    return response  # ส่งกลับคำตอบที่สมบูรณ์

# API สำหรับรับข้อความจากผู้ใช้และตอบกลับด้วยข้อความจากแชทบอท
@app.route('/api/message', methods=['POST'])
def api_message():
    # รับข้อความผู้ใช้จาก request (ในรูปแบบ JSON)
    user_message = request.json.get('message', '')
    # เรียกใช้ฟังก์ชัน respond เพื่อสร้างคำตอบ
    bot_response = respond(user_message)
    # ส่งคำตอบกลับในรูปแบบ JSON
    return jsonify({'response': bot_response})

# API สำหรับวิเคราะห์ความรู้สึกของข้อความผู้ใช้ (Sentiment Analysis)
@app.route('/api/sentiment', methods=['POST'])
def api_sentiment():
    # รับข้อความผู้ใช้จาก request
    user_message = request.json.get('message', '')
    # ใช้ VADER sentiment analysis ในการประเมินความรู้สึกของข้อความ
    sentiment_scores = sid.polarity_scores(user_message)
    # ส่งคะแนนความรู้สึกกลับในรูปแบบ JSON
    return jsonify(sentiment_scores)

# ฟังก์ชันสำหรับแสดงหน้าเว็บหลัก
@app.route('/')
def index():
    return render_template('index.html')  # ชี้ไปที่ไฟล์ HTML (index.html)

# เริ่มการทำงานของแอปพลิเคชัน Flask
if __name__ == '__main__':
    # รันแอปพลิเคชันในโหมด debug เพื่อให้สามารถดูข้อผิดพลาดได้ง่ายขึ้น
    app.run(debug=True)
