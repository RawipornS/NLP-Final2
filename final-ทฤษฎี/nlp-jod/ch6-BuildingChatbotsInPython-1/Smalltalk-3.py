responses = {
    "what's your name?": [
        "my name is EchoBot",
        "they call me EchoBot",
        "the name's Bot, EchoBot"
    ]
}
import random
def respond(message):

    if message in responses:

        return random.choice(responses[message])

print(respond("what's your name?"))