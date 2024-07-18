import requests

# Make a GET request to an API endpoint
response = requests.get('https://api.example.com/data')

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and retrieve the value associated with the key "value"
    data = response.json()
    value = data.get("value")

    if value is not None:
        print(f"The value obtained from the JSON response is: {value}")
    else:
        print("The key 'value' is not present in the JSON response.")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}")
