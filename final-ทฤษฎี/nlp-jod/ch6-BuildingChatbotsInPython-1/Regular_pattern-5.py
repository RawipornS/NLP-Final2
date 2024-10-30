import random
import re  

rules = {
    'do you think (.*)': [
        'If {0}? Absolutely.',
        'No chance.'
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
        'Really--if {0}.'
    ]
}

bot_template = "BOT: {0}"

# match_rule function
def match_rule(rules, message):
    response, phrase = "default", None
    for pattern, responses in rules.items():
        match = re.match(pattern, message)
        if match is not None:
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    return response.format(phrase) if phrase else response

def respond(message):
    return match_rule(rules, message)

def send_message(message):
    response = respond(message)
    print(bot_template.format(response))

while True:
    user_message = input("USER: ")
    if user_message.lower() == "bye":
        print("BOT: Goodbye!")
        break
    send_message(user_message)
