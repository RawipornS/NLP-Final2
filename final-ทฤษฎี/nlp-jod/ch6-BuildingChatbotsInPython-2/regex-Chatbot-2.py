intents_patterns = {
    'greet': ['hello', 'hi', 'hey'],
    'goodbye': ['bye', 'goodbye'],
    'thankyou': ['thanks', 'thank you', 'thankyou']
}

def match_intent(message):
    matched_intent = None
    for intent, patterns in intents_patterns.items():
        if any(pattern in message.lower() for pattern in patterns):
            matched_intent = intent
            break  
    return matched_intent

def respond(message):
    intent = match_intent(message)
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Define responses
responses = {
    'greet': 'Hello you! :)',
    'goodbye': 'Goodbye for now',
    'thankyou': 'You are very welcome',
    'default': 'Default message'
}

bot_template = "BOT : {0}"
user_template = "USER : {0}"

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")
