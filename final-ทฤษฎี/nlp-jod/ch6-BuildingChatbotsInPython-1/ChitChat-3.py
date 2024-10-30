import random

bot_template = "Bot : {0}"

responses = {
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
    
    if message.endswith('?'):
        return random.choice(responses['question'])
    return random.choice(responses['statement'])

def send_message(message):
    respond(message)
    print(bot_template.format(responses))

# Test the functions
# print(respond("what's today's weather?"))
# print(respond("what's today's weather?"))
# print(respond("I love building chatbots"))
# print(respond("I love building chatbots"))

while True:
    user_message = input('USER: ')
    if user_message.lower() == 'bye':
        print('BOT: Good BYE !')
        break

    print('BOT:', send_message(user_message))
