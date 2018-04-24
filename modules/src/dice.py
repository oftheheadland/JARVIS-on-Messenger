import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
    1: 'https://gfycat.com/UnconsciousLegalDoe',
    2: 'https://gfycat.com/UnconsciousLegalDoe',
    3: 'https://gfycat.com/UnconsciousLegalDoe',
    4: 'https://gfycat.com/UnconsciousLegalDoe',
    5: 'https://gfycat.com/UnconsciousLegalDoe',
    6: 'https://gfycat.com/UnconsciousLegalDoe',
}


def process(input, entities=None):
    message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='gif').get_message()
    message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
