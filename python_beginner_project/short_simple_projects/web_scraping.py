# to get the image link of the profile image of a particular GitHub user
import requests
from bs4 import BeautifulSoup as bs

github_user = input("enter Github Username: ")

# in web scraping, you need to send a request to the url and get the whole HTML of the page

url = "https://github.com" + github_user

request = requests.get(url)  # sends a request to the url
soup = bs(request.content, "html.parser") # request to get the HTML source code
DP = soup.find("img", {"alt" : "avatar"})["src"] # finding a specific tag

print(DP)
