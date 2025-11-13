EMOTION_RESPONSES = {
    "happy": "😊 You're having a good day!",
    "sad": "😢 You're having a bad day. Are you okay?",
    "angry": "😠 You're having an angry day",
    "excited": "🤩 You're having an excited day!",
    "bored": "😐 You're having a bored day",
    "confused": "😕 You're having a confused day",
    "?": "🤔 I am not sure about your feeling",
    "!": "😲 I am surprised to hear that!",
}


def analyze_emotions(message):
    words = message.lower().strip().split()
    # 
    responses = []
    for word in words:
        if word in EMOTION_RESPONSES:
            responses.append(EMOTION_RESPONSES[word])
    # 
    if responses:
        for response in responses:
            print(response)
    else:
        print("No emotions detected. Please try again!")



user_input = input("hey i am imma , feel free to ask 🖤 : ")
analyze_emotions(user_input)