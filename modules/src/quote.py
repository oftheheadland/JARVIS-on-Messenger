import json
from random import choice
import requests
import sys
from bs4 import BeautifulSoup
import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        url = "https://www.brainyquote.com/link/quotebr.rss"
        # request to dowmload website content
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        contentVar = soup.currentTag
        titleVar = contentVar.findAll('title')
        descVar = contentVar.findAll('description')

        titleQu = titleVar[2]
        descQu = descVar[2]

        quoteDay = titleQu + " : " + descQu


        #with open(config.QUOTES_SOURCE_FILE) as quotes_file:
            #quotes = json.load(quotes_file)
            #quotes_list = quotes['quotes']
        #message = TextTemplate(choice(quoteDay)).get_message()
            #message = add_quick_reply(message, 'Another one!', modules.generate_postback('quote'))
        #message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
        #message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
        output['input'] = input
        output['output'] = TextTemplate(choice(quoteDay)).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
