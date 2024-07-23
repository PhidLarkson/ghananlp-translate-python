# this python script is for Twi, check out the GhanaNLP website for more language options.

import requests

def translate(text, target_language):
    url = "https://translation-api.ghananlp.org/v1/translate"
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': 'YOUR API KEY HERE',
    }
    data = {
        'in': text,
        'lang': target_language
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
         return response.json()
    else:
         return "An error occured"

language_choice = "en-tw"

print("Welcome to the GhanaNLP translator program")

while True:    
     try:
          message = input("Type what you want to translate in English: ")
          translation = translate(message, language_choice)
     except:
          pass
     
     print(f"Translation to Twi:{translation}\n")
