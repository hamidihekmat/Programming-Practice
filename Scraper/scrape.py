import requests
from bs4 import BeautifulSoup

link = 'https://www.mangareader.net/dr-stone/1'

headers = {
'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
}


page = requests.get(link, headers=headers)


soup = BeautifulSoup(page.content, 'html.parser')

menu = soup.find(id='pageMenu').get_text()

pages = (menu.split())

max_page = int(pages[-1])

images = soup.findAll('img')

# for image in images:
#     print(image['src'])


def get_pages(link, max):
    pages = []
    for page in range(1, max+1):
        pages.append(link + '/{}'.format(page))
    return pages



def get_images(links): #links of pages
    images = []
    headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    for link in links:
        page = requests.get(link, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        image = soup.findAll('img')
        for img in image:
            images.append(img['src'])
    return images


def create_file(images):
    with open('chapters.txt','a') as f:
        for img in images:
            f.write(img +'\n')



stone = get_pages(link, max_page)
list_image = get_images(stone)
create_file(list_image)
