name = "Bot"
weather = "cloudy"

responses = {
    "what's your name?": "my name is {0}".format(name),
    "what's today's weather?": "the weather is {0}".format(weather),
    "default": "default message"
}

# Return the matching response if there is one, default otherwise
def send_message(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

# Main loop
while True:
    messages = input('USER: ')
    if messages.lower() == 'bye':
        print('BOT: Good BYE !')
        break

    print('BOT:', send_message(messages))

