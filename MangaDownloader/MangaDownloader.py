import requests
import os
import io
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
        image = requests.get(image).content
        with open(filename, 'wb') as img:
            img.write(image)
        print('{} is done downloading!'.format(filename))


    def batchDownload(self):
        '''
        Downloads all the pages for the given chapter
        '''
        images = self.getImages()
        counter = 1
        for image in images:
            file_name = 'manga{}.jpg'.format(counter)
            t = Thread(target=self.imageDownload, args=[image, file_name])
            t.start()
            t.join()
            counter += 1

    def makePDF(self):
        print(self.title)
        self.batchDownload()

        # get list image names
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



# Example donwload

drStone = 'https://www.mangareader.net/dragon-ball/1'
MangaDownloader(drStone).makePDF()
# MangaDownloader(drStone).batchDownload()
# MangaDownloader(drStone).createFile()
