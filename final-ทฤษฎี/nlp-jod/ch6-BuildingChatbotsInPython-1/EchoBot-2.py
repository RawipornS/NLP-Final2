bot_template = "BOT : {0}"
user_template = "USER : {0}"


def respond(message):
    # Concatenate the use's message to the end of a standard bot repone
    bot_message = 'I can hear you! You said : ' + message
    return bot_message

# define a function that responds to a user's
def send_message(message):
    print(user_template.format(message))

    response = respond(message)

    print(bot_template.format(response))

send_message('hello')
