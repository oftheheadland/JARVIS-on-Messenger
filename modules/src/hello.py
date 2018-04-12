import random

from templates.text import TextTemplate


def process(input, entities=None):
    greetings = [
        'Salutations! Enter a command, user!',
        'Yes? Tell me to do something, user.',
        'Hello! How can I be of service?',
        'At your service, user.',
        'Oh hello, user!',
        'Jarvis, reporting in. How can I help you today, user?',
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
