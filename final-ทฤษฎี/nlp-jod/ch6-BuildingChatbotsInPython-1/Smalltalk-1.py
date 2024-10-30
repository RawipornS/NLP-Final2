
responses = {
    "What's your name?":"my name is Echobot",
    "What's the weather today?":"it's sunny !"
}

def respond(message):
    if message in responses:
        return responses[message]
print(respond("What's your name?"))
