import requests
from bs4 import BeautifulSoup

URL = 'https://vidstreaming.io/videos/dr-stone-dub-episode-7'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.post(URL, headers=headers)

#soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

#video = soup.find('iframe').get('src')
#video = soup.find('div', {'class': 'watch_play'})
#print(video)
print(page)
