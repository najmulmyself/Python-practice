import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gsmarena.com/samsung-phones-9.php'
r = requests.get(url)
html = bs(r.text,'html.parser')
# eTitle = html.find_all('div', {"class" : "job_seen_beacon"})
# for tag in eTitle:
#     title = tag.find_all('h2')
#     for loc in title:
#         print(loc.text)


# jobD = html.find_all('div', {"class" : "jobsearch-jobDescriptionText"})
# for p in jobD:
#     # des = p.find_all(p.text)
#     print(p)

# print(jobD)

divPhone = html.find('div',{'class':'makers'})
# titlePhone= divPhone[0].findAll('span').text

# print(type(divPhone))

# title = divPhone.find_all('span')

# for titlePhone in divPhone:
#     titlePhone.findAll('span')
#     print(titlePhone)

spanPhone = divPhone.find_all('span')
for titlePhone in spanPhone:
    print(titlePhone.text)