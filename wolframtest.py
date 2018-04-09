import wolframalpha
import os
from datetime import datetime
import requests
import config
from templates.text import TextTemplate
from templates.button import *

output = {}


#math = entities['math'][0]['value']
app_id = "QQX2TL-VJ2HWY454T"
client = wolframalpha.Client(app_id)

response = "1*2"
#res = client.query(response)
res = client.query("5/5")

counter = 0
for pod in res.pods:
    texts = "input: " + pod.text + "\n"
    if counter > 0:
        texts += "result: " + pod.text
        break
    counter += 1

texts = texts.encode('ascii', 'ignore')
print(texts)



    # to skip ascii character in case of error
    #texts = texts.encode('ascii', 'ignore')
    #print(texts)

print(texts)





