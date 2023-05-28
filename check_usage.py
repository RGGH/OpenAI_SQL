
# Set your OpenAI API key
api_key = "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"

import requests
from datetime import date
from pprint import pprint
# Set your OpenAI API key

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

# Make the GET request to retrieve usage information
response = requests.get(usage_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the usage information
# Extract the response JSON
    usage_data = response.json()

    # Initialize the token count
    token_count = 0

    # Iterate over each item in the usage data
    for item in usage_data["data"]:
        # Add up the token count
        token_count += (item["n_generated_tokens_total"] + item['n_context_tokens_total'])

    # Print the total token count
    print("Total Token Count:", token_count)
    print(f"Cost = ", token_count * 0.02 * 0.001)
else:
    # Print the error message if the request failed
    print(f"Request failed with status code: {response.status_code}")
    print(response.json())

