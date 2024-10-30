import random

name = "Bot"
weather = "cloudy"
responses = {
    "what's your name?": [
        "my name is {0}".format(name),
        "they call me {0}".format(name),
        "I am {0}".format(name)
    ],
    "what's today's weather?": [
        "the weather is {0}".format(weather),
        "it's {0} today".format(weather)
    ],
    'statement': [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way?',
        'I find that extremely interesting',
        'can you back that up?', 'oh wow!',
        ':)'
    ],
    'question': [
        "I don't know :(",
        'you tell me!'
    ],
    "default": ["default message"]
}

def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

while True:
    user_message = input('USER: ')
    if user_message.lower() == 'bye':
        print('BOT: Good BYE !')
        break

    print('BOT:', respond(user_message))
