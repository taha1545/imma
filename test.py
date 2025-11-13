EMOTION_RESPONSES = {
    "happy": "😊 You're having a good day!",
    "sad": "😢 You're having a bad day. Are you okay?",
    "angry": "😠 You're having an angry day",
    "excited": "🤩 You're having an excited day!",
    "bored": "😐 You're having a bored day",
    "confused": "😕 You're having a confused day",
}

GREETING_RESPONSES = {
    "hello": "👋 Hi there! I'm Imma, nice to meet you!",
    "hey": "👋 Hey! What's up?",
    "hi": "👋 Hello! How are you?",
    "who": "🤖 I'm Imma, your emotion analyzer. Tell me how you feel!",
    "about": "🤖 I'm here to listen and understand your emotions!",
    "salam" :"  👋 Waalaikumussalam! How can I assist you today?",
}

SPECIAL_RESPONSES = {
    "?": "🤔 I'm not sure, but I'm here to help!",
    "!": "😲 Wow, that sounds interesting!",
}


def analyze_emotions(message):
    #
    words = message.lower().strip()
    word_list = words.split()
    #
    print("\n ANALYSIS .....")
    # Check for greetings
    greeting_found = False
    for greeting, response in GREETING_RESPONSES.items():
        if greeting in words:
            print(response)
            greeting_found = True
            break
    # Check for emotions
    emotions_found = []
    for word in word_list:
        if word in EMOTION_RESPONSES:
            emotions_found.append(EMOTION_RESPONSES[word])
    
    if emotions_found:
        print("\n📊 Emotions Detected:")
        for emotion in emotions_found:
            print(f"  • {emotion}")
    
    # Check for special characters
    if "?" in message:
        print(f"\n{SPECIAL_RESPONSES['?']}")
    if "!" in message:
        print(f"\n{SPECIAL_RESPONSES['!']}")
    
   
    # 
    if len(word_list) > 10:
        print("  • 📝 That's detailed! I'm listening carefully...")
    elif len(word_list) <= 2:
        print("  • 💭 Short message. Tell me more!")
    
    # 
    if not emotions_found and not greeting_found:
        print(f"\n🤔 Interesting! How does that make you feel?")


#
if __name__ == "__main__":
    user_input = input("Hey, I'm Imma! 🖤 Tell me how you feel: ")
    analyze_emotions(user_input)