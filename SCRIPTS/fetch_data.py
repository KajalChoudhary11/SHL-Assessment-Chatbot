import requests
import json

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"
response = requests.get(url)                            #fetching allthe data from rhe catalog using the url provided by SHL
data = json.loads(response.text, strict = False)        #we used loads instead of response.json() because the data contains some special characters which are not handled by the default json

with open('DATA/shl_catalog.json','w') as f:            #fetched all the data and saved in a json file for future use
    json.dump(data,f,indent = 4)

print("Data fetched and saved successfully through SHL catalog!")
print(f"total items fetched:{len(data)}")

