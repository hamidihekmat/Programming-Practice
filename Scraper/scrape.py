import requests
from bs4 import BeautifulSoup
from threading import Thread
link = 'https://www.mangareader.net/one-piece/955'

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




def download_images(image, filename):
    image = requests.get(image).content
    with open(filename, 'wb') as img:
        img.write(image)
    print('{} is done downloading!'.format(filename))


def thread_download(list_image):
    counter = 1
    for image in list_image:
        file_name = 'manga{}.jpg'.format(counter)
        t = Thread(target=download_images, args=[image, file_name])
        t.start()
        counter += 1


all_pages = get_pages(link, max_page)
list_image = get_images(all_pages)
#create_file(list_image)
thread_download(list_image)

# concurrently download managa pages
