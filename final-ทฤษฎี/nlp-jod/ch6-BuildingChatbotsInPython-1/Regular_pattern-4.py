rules = {
    'do you think (.*)': [
        'if {0}? Absolutely.',
        'No chance'
    ],
    'do you remember (.*)': [
        'Did you think I would forget {0}?',
        "Why haven't you been able to forget {0}?",
        'What about {0}?',
        'Yes .. and?'
    ],
    'I want (.*)': [
        'What would it mean if you got {0}?',
        'Why do you want {0}?',
        "What's stopping you from getting {0}?"
    ],
    'if (.*)': [
        "Do you really think it's likely that {0}?",
        'Do you wish that {0}?',
        'What do you think about {0}?',
        'Really--if {0}'
    ]
}

import random
import re

def match_rule(rules, message):
    response, phrase = "default", None
    for pattern, responses in rules.items():
        match = re.match(pattern, message)
        if match is not None:
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)

    return response.format(phrase)

# Test match_rule
# print(match_rule(rules, "do you remember your last birthday"))

# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return message.replace('me', 'you')
    if 'my' in message:
        # Replace 'my' with 'your'
        return message.replace('my', 'your')
    if 'your' in message:
        # Replace 'your' with 'my'
        return message.replace('your', 'my')
    if 'you' in message:
        # Replace 'you' with 'me'
        return message.replace('you', 'me')
    return message

# Test replace_pronouns
# print(replace_pronouns("my last birthday"))
# print(replace_pronouns("go with me to Florida"))
# print(replace_pronouns("I had my own castle"))

def respond(message):
    response, phrase = match_rule(rules, message), None

    if '{0}' in response:
        phrase = replace_pronouns(phrase)
        response = response.format(phrase)
    
    return response

# Define send_message (for testing purpose)
def send_message(message):
    print(f"User: {message}")
    print(f"Bot: {respond(message)}")
    print()

# Send the messages
send_message("do you remember my last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("if you could be anything you wanted")
