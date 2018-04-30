import random

import modules
from templates.attachment import AttachmentTemplate
from templates.text import TextTemplate
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
	#Get all digits in input, use first digit found as number of sides
	sides = [int(s) for s in input.split(" ") if s.isdigit()]
	#Roll a 6 sided die if desired sides was 6, 0, or unspecified
	print(sides)
	if len(sides) == 0 or sides[0] == 6 or sides[0] == 0:
		message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
		message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
		message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
		output = {
			'input': input,
			'output': message,
			'success': True
		}
		return output
	#Otherwise roll a die with the specified number of sides
	else:
		message = TextTemplate("You rolled a " + str(random.randint(1, sides[0])) + ".").get_message()
		message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
		message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
		output = {
			'input': input,
			'output': message,
			'success': True
		}
		return output