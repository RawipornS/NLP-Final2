import re
def swap_pronouns(phrase):

    if 'I' in phrase:
        return re.sub('I', 'You', phrase)

    if 'My' in phrase:
        return re.sub('My', 'Your', phrase)

    if 'Your' in phrase:
        return re.sub('Your', 'My', phrase)
    
    if 'You' in phrase:
        return re.sub('You', 'Me', phrase)
    
    else:
        return phrase

print(swap_pronouns("I walk to school"))
print(swap_pronouns("Your last birthday"))
print(swap_pronouns("Go with You to florida"))