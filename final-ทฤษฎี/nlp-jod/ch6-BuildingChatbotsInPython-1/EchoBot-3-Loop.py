bot_template = "BOT : {0}"
user_template = "USER : {0}"


def respond(message):
    bot_message = 'I can hear you! You said : ' + message
    return bot_message

def send_message():
    while True:
        message = input('USER: ')
        if message.lower() == 'bye':
            print('BOT: Good BYE !')
            break

        response = respond(message)

        print(bot_template.format(response))

send_message()
