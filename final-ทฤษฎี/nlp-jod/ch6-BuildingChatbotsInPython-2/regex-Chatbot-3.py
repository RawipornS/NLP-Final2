import re

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

# Define responses
responses = {
    'greet': 'Hello you! :)',
    'goodbye': 'Goodbye for now',
    'thankyou': 'You are very welcome',
    'default': 'Default message'
}

bot_template = "BOT : {0}"
user_template = "USER : {0}"

def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile(r'\b(my name is|call me|people call me)\b', re.I)
    # Create a pattern for finding capitalized words
    name_pattern = re.compile(r'\b[A-Z][a-z]*\b')
    
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    
    return name

def respond(message):
    # First, check for a name
    name = find_name(message)
    if name is None:
        # If no name is found, check for intent
        intent = match_intent(message)
        key = "default"
        if intent in responses:
            key = intent
        return responses[key]
    else:
        return "Hello, {0}!".format(name)

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

# Send messages

send_message("my name is David Copperfield")  # Name extraction
send_message("call me Ishmael")           # Name extraction
send_message("people call me Cassandra")   # Name extraction
send_message("I walk to school")           # No intent
