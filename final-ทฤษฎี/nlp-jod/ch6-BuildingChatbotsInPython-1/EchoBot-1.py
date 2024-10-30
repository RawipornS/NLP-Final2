bot_template = "BOT : {0}"
user_template = "USER : {0}"


# define a function that responds to a user's
def respond(message):
    # Concatenate the use's message to the end of a standard bot repone
    bot_message = 'I can hear you! You said : ' + message
    return bot_message

print(respond('hello'))