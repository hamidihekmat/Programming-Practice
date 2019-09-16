import requests
from bs4 import BeautifulSoup
from threading import Thread



class MangaDownloader:
    '''
    Download manga chapters from (https://www.mangareader.net)
    '''
    def __init__(self, mangaLink):
        self.headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
        }
        self.mangaLink = mangaLink
        self.manga = requests.get(self.mangaLink, headers=self.headers).content
        self.pages = self.get_pages()

    def get_pages(self):
        '''
        Returns list of pages
        '''
        soup = BeautifulSoup(self.manga, 'html.parser')
        menu = soup.find(id='pageMenu').get_text()
        pages = (menu.split())
        max_page = int(pages[-1])

        pages = []
        for page in range(max_page):
            pages.append(self.mangaLink + '/{}'.format(page))
        return pages

    def get_images(self):
        '''
        Returns list of image links
        '''
        images = []

        for link in self.pages:
            page = requests.get(link, headers=self.headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            image = soup.findAll('img')
            for img in image:
                images.append(img['src'])
        return images

    def createFile(self):
        '''
        Creates a file containing the img links
        '''
        images = self.get_images()
        with open('chapters.txt','a') as f:
            for img in images:
                f.write(img +'\n')


    def imageDownload(self, image, filename):
        '''
        Downloads image (page) from a link
        '''
        image = requests.get(image).content
        with open(filename, 'wb') as img:
            img.write(image)
        print('{} is done downloading!'.format(filename))


    def batchDownload(self):
        '''
        Downloads all the pages for the given chapter
        '''
        images = self.get_images()
        counter = 1
        for image in images:
            file_name = 'manga{}.jpg'.format(counter)
            t = Thread(target=self.imageDownload, args=[image, file_name])
            t.start()
            t.join()
            counter += 1



# Example donwload

one_piece = 'https://www.mangareader.net/hunter-x-hunter/4'
MangaDownloader(one_piece).batchDownload()
