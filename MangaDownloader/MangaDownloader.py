import requests
import os
import math
from os import system
import io, time, asyncio
import img2pdf
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
        self.pages = self.getPages()
        self.title = self.setTitle()
        self.downloads = 0

    def setTitle(self):
        soup = BeautifulSoup(self.manga, 'html.parser')
        title = soup.find(class_='c4').get_text().strip()
        return str(title)


    def getPages(self):
        '''
        Returns list of pages
        '''
        soup = BeautifulSoup(self.manga, 'html.parser')
        menu = soup.find(id='pageMenu').get_text()
        title = soup.find(class_='c4').get_text().strip()
        pages = (menu.split())
        max_page = int(pages[-1])

        pages = []
        for page in range(1, max_page + 1):
            pages.append(self.mangaLink + '/{}'.format(page))
        return pages

    def getImages(self):
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
        images = self.getImages()
        with open(self.title +".txt",'a') as f:
            for img in images:
                f.write(img +'\n')


    def imageDownload(self, image, filename):
        '''
        Downloads image (page) from a link
        '''
        running = True
        tries = 4
        while running:
            try:
                image = requests.get(image).content
                with open(filename, 'wb') as img:
                    img.write(image)
                    time.sleep(1)
                    running = False
            except:
                running = True
                tries -= 1
                if tries == 0:
                    running = False

        return True #print('{} is done downloading!'.format(filename))

    async def batchDownload(self):
        '''
        Downloads all the pages for the given chapter
        '''
        print(self.title)
        self.images = []
        counter = 1
        amt = 2
        for i in range(1, amt):
            t = self.getImages()
            for j in t:
                l = len(t) * amt
                print("Download progress: "+self.loading(l, counter))
                counter += 1
                self.images.append(j)
        counter = 1
        threads = []
        for image in self.images:
            file_name = 'manga{}.jpg'.format(counter)
            t = (Thread(target=self.imageDownload, args=[image, file_name]))
            threads.append(t)

            counter += 1
        for thread in threads:
            thread.start()
            self.downloads +=1
            print("Writing progress: "+self.loading(len(self.images), self.downloads))
        await asyncio.sleep(5)
        return "hi"


    def scan(self):
        imagelist = []
        for image in os.listdir('.'):
            if image.endswith('.jpg'):
                imagelist.append(image)
        for i in range(len(imagelist)):
            imagelist[i] = "manga{}.jpg".format(i+1)

        # write the pdf file
        with open(self.title+".pdf", "wb") as f, io.BytesIO() as output:
            f.write(img2pdf.convert(imagelist))
        # remove images
        for image in imagelist:
            os.remove(image)

    def test(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.batchDownload())
        time.sleep(1)
        self.scan()
        print("Done")

    def loading(self, size, amount):
        system('clear')
        sr = "["
        state = math.floor((amount/size*100)/5)
        for i in range(state):
            sr = sr+"#"
        for i in range(20-state):
            sr = sr+" "
        sr = sr+"]"
        sr = '{} %{}'.format(sr, int((amount/size*100)))
        return sr


# Example donwload

naruto1 = 'https://www.mangareader.net/bleach/4'
MangaDownloader(naruto1).test()
# MangaDownloader(drStone).batchDownload()
# MangaDownloader(drStone).createFile()
