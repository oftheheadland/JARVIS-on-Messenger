import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

# Images by US Mint; published on wikimedia under public domain rights
coin_images = {
    'heads': 'https://thumbs.gfycat.com/MisguidedImportantDiscus-size_restricted.gif',
    'tails': 'https://thumbs.gfycat.com/RareFloweryAruanas-size_restricted.gif'
}


def process(input, entities=None):
    message = AttachmentTemplate(coin_images[random.choice(['heads', 'tails'])], type='image').get_message()
    message = add_quick_reply(message, 'Flip again!', modules.generate_postback('coin'))
    message = add_quick_reply(message, 'Roll a die.', modules.generate_postback('dice'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
