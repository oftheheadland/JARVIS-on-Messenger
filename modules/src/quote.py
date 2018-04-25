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
        # contentVar = soup.currentTag
        # titleVar = soup.findAll('title')
        # descVar = soup.findAll('description')

        title_tag = soup.findAll("title")[2]
        description_tag = soup.findAll("description")[2]
        # print(title_tag.text)
        # print(description_tag.text)
        quotes = (title_tag.text + ' ; ' + description_tag.text)


        #with open(config.QUOTES_SOURCE_FILE) as quotes_file:
            #quotes = json.load(quotes_file)
            #quotes_list = quotes['quotes']
        message = TextTemplate(choice(quotes)).get_message()
            #message = add_quick_reply(message, 'Another one!', modules.generate_postback('quote'))
        message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
        message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output
