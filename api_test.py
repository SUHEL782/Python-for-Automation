import requests


demo_url = "https://random-data-api.com/api/v3/projects/03fe15d9-9486-4abb-87e0-97e96957e49b?api_key=9hoRR4-VIWMiJS505lA1KA"
# Define the base URL for the API
res =requests.get(url=demo_url)
print(res.status_code) # Print the status code of the response
print(type(res.json()) )# Print the JSON response from the API
print(res.json()) 
# Print the content of the response
# print(res.content) # Print the content of the response
# Print the headers of the response


