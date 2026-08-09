import requests # pip install requests

a = requests.get("https://api.github.com/")
print(a.json()) # here we are using the json() method to convert the response into a JSON object. We can also use the text attribute to get the response as a string. The json() method is used to parse the JSON response and convert it into a Python dictionary. The text attribute returns the response as a string.