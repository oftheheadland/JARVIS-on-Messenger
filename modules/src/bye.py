import random

from templates.text import TextTemplate


def process(input, entities=None):
    greetings = [
        'Have a good day, user.',
        'Wonderful, I think it\'s time for my evening nap...',
        'Bye to you as well, user.',
        'It was my pleasure talking to you.',
        'It\'s sad to see you leave.',
        'Farewell! I hope I will see you soon.',
    ]
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            sender_name = entities['sender']['first_name']
            greetings = [greeting.replace('user', sender_name) for greeting in greetings]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
