import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
    1: 'https://thumbs.gfycat.com/NewFoolhardyAvocet-size_restricted.gif',
    2: 'https://thumbs.gfycat.com/ShyCelebratedGraywolf-size_restricted.gif',
    3: 'https://thumbs.gfycat.com/SeriousPiercingBangeltiger-size_restricted.gif',
    4: 'https://thumbs.gfycat.com/AdoredFirmLcont-size_restricted.gif',
    5: 'https://thumbs.gfycat.com/FrequentQueasyEgg-size_restricted.gif',
    6: 'https://thumbs.gfycat.com/WanTameAfricanparadiseflycatcher-size_restricted.gif',
}


def process(input, entities=None):
    message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
    message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
