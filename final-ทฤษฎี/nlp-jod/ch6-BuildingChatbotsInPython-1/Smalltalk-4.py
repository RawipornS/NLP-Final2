responses = ["tell me more!", "why do you think that?"]
import random
def respond(message):

    return random.choice(responses)
print(respond("I think you're really great"))