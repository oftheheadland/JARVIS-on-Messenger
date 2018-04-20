import wolframalpha






import os
from datetime import datetime

import requests

import config
from templates.text import TextTemplate
from templates.button import *

def process(input, entities):
    output = {}
    try:
        # math = entities['math'][0]['value']
        app_id = "QQX2TL-VJ2HWY454T"
        client = wolframalpha.Client(app_id)

        response = "1*2"
        # res = client.query(response)
        input = input.replace("math", "")
        res = client.query(input)
        texts = ""
        counter = 0
        for pod in res.pods:
            #if counter == 0:
            #    texts = "input: " + pod.text + "\n"
            #    texts = texts.encode('ascii', 'ignore')
            if counter > 0:
                texts += pod.text
                break
            counter += 1


        #texts = texts.encode('ascii', 'ignore')
        #print(texts)

        #output['input'] = input
        output['input'] = ''
        output['output'] = TextTemplate('Result from wolframpalpha: ' + texts).get_message()
        #output['output'] = texts
        output['success'] = True
    except:
        error_message = 'I couldn\'t get the right answer for that.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - 3/2'
        error_message += '\n  - 5 squared'
        error_message += '\n  - 5*3'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output






