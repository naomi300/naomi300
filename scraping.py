from cgi import print_arguments


import requests
from bs4 import BeautifulSoup as bs

user_name = "naomi300" #input("enter your user name ")

url ="https://github.com/" + user_name #input("enter site url") 
result = requests.get(url)

soup = bs(result.content,"html.parser")
profile_pic = soup.find("img",{"alt":"Avatar"})["src"]
print(profile_pic)






