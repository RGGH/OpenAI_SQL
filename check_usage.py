"""
Check token usage of OpenAI and multiply by corresponding model price
https://redandgreen.co.uk
Python 360 ~ https://www.youtube.com/@python360
"""


# Set your OpenAI API key
api_key = "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"

import requests
from datetime import date
from pprint import pprint


snapshot_id = {
  "text-davinci:003": 0.002,
  "text-embedding-ada-002-v2": 0.02,
}


# Set the API endpoint for usage
usage_url = "https://api.openai.com/v1/usage"

# Set the headers with your API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set the query parameters
#today = date.today().isoformat() 
params = {
    "date":"2023-05-24" 
}

pricing = {
  "text-davinci:003": 0.02,
  "text-embedding-ada-002-v2": 0.0004,
}

# Make the GET request to retrieve usage information
response = requests.get(usage_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the response JSON
    usage_data = response.json()

    list =[] # create empty list
    for val in usage_data['data']: 
        cost = ((
            val['n_context_tokens_total'] *  pricing[val['snapshot_id']]
            +
            val['n_generated_tokens_total'] *  pricing[val['snapshot_id']]
            ) * 0.001)


        list.append(cost)

    print (sum(list))
    
else:
    # Print the error message if the request failed
    print(f"Request failed with status code: {response.status_code}")



