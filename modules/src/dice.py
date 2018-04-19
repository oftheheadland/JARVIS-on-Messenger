import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply
diceAnim = {
    1: 'https://gfycat.com/UnconsciousLegalDoe',
    2: 'https://gfycat.com/UnconsciousLegalDoe',
    3: 'https://gfycat.com/UnconsciousLegalDoe',
    4: 'https://gfycat.com/UnconsciousLegalDoe',
    5: 'https://gfycat.com/UnconsciousLegalDoe',
    6: 'https://gfycat.com/UnconsciousLegalDoe',
}

dice_sides = {
    1: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-one/256/0/e74c3c_none.png',
    2: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-two/256/0/e74c3c_none.png',
    3: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-three/256/0/e74c3c_none.png',
    4: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-four/256/0/e74c3c_none.png',
    5: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-five/256/0/e74c3c_none.png',
    6: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-six/256/0/e74c3c_none.png'
}


def process(input, entities=None):
    message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
    message  = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    message2 = AttachmentTemplate(diceAnim[random.randint(1, 6)], type='image').get_message()
    output = ( {
        'input': input,
        'output': message,
        'success': True
    },
    {
        'input': input,
        'output': message2,
        'success': True
    }
    )
    return output
