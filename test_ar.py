from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------------------
#   Emotion & Greeting Data
# ---------------------------

EMOTION_RESPONSES = {
    "سعيد": "😊 يبدو أنك سعيد اليوم!",
    "فرح": "😄 يومك جميل ومليء بالسعادة!",
    "حزين": "😢 يبدو أنك حزين... هل تريد التحدث عن ذلك؟",
    "غاضب": "😠 تشعر بالغضب... خذ نفساً عميقاً.",
    "متوتر": "😰 أشعر أنك متوتر... أنا هنا معك.",
    "متحمس": "🤩 يا لها من طاقة! أنت متحمس جداً!",
    "ضايق": "😕 يبدو أنك منزعج قليلاً.",
    "ملل": "😐 تشعر بالملل... لنحاول تغيير الجو!",
}

GREETING_RESPONSES = {
    "سلام": "👋 وعليكم السلام! كيف يمكنني مساعدتك؟",
    "مرحبا": "👋 مرحباً! أنا إيما، يسعدني التحدث معك!",
    "اهلا": "👋 أهلاً! كيف تشعر اليوم؟",
    "هاي": "👋 هاي! كيف يومك؟",
    "من": "🤖 أنا إيما، محللة المشاعر الخاصة بك. أخبرني ما تشعر به!",
    "عن": "🤖 أنا هنا لأسمعك وأفهم مشاعرك 💛",
}

SPECIAL_RESPONSES = {
    "?": "🤔 سؤال جميل… هل تريد توضيح المزيد؟",
    "!": "😲 يبدو أنك متأثر جداً بما قلت!",
}


# ---------------------------
#     Core Analyzer Logic
# ---------------------------
def analyze_emotions(message):
    text = message.lower().strip()
    words = text.split()

    result_parts = []

    # 1. تحليل التحيات
    for greeting, response in GREETING_RESPONSES.items():
        if greeting in text:
            result_parts.append(response)
            break

    # 2. تحليل المشاعر
    for word in words:
        if word in EMOTION_RESPONSES:
            result_parts.append(EMOTION_RESPONSES[word])

    # 3. رموز خاصة
    if "؟" in message or "?" in message:
        result_parts.append(SPECIAL_RESPONSES["?"])

    if "!" in message:
        result_parts.append(SPECIAL_RESPONSES["!"])

    # 4. طول النص
    if len(words) > 10:
        result_parts.append("📝 رسالتك طويلة… يبدو أنك تفكر كثيراً.")
    elif len(words) <= 2:
        result_parts.append("💭 رسالتك قصيرة… قل لي المزيد!")

    # 5. لا شيء مفهوم
    if not result_parts:
        result_parts.append("🤔 فهمت… لكن كيف يجعلك هذا تشعر؟")

    return " ".join(result_parts)


# ---------------------------
#       Flask Route
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("user_text", "")
        result = analyze_emotions(input_text)

    return render_template("mood_analyzer.html",
                           result=result,
                           input_text=input_text)


# ---------------------------
#      Run Server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
