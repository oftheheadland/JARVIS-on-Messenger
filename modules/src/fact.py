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
        url = "http://unbelievablefactsblog.com/rss"
        # request to dowmload website content
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        description_tag = soup.findAll('description')[1]
        textMe = description_tag.text

        start = textMe.find('<p>') + 3
        end = textMe.find('<br/>', start)
        #facts = json.load(facts_file)
        #facts_list = facts['facts']





        message = TextTemplate(textMe[start:end]).get_message()
        #message = add_quick_reply(message, 'Another fact!', modules.generate_postback('fact'))
        message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
        message = add_quick_reply(message, 'Show me a quote.', modules.generate_postback('quote'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output
