import requests
from bs4 import BeautifulSoup
import json

# Implementation to make a json file from html file    
def json_maker(self):
    print("Creating JSON file [may take few seconds...]")
    with open(self.fetched_data, 'r') as f:             # reading the html file
        self.html_data = f.read()
    
    tags = BeautifulSoup(self.html_data, 'lxml').find_all('a')  # Fetching all the "a" tags

    with open(self.storage, 'w') as f:                  # writing all the parsed results to a json file for better navigation
        for tag in tags:
            self.stark[f"{tag.text}"] = ""
        json.dump(self.stark, f)

    with open(self.storage, 'r') as f:                  # Reading the same json file and fetching all the keys into a dict
        self.all_repos = json.load(f).keys()
        # print(all_repos)

# Function to make a request to pypi and get all the package's names
def fetch(self):
    print("Fetching the data!")
    response = requests.get(self.fetch_url).text   # make the request
    print("Request completed")
    with open(self.fetched_data, 'w') as f:         # write the fetched HTML code to a html file
        f.write(response)
    json_maker(self)                               # Parse the html file and create a json file
    print("JSON file created")
