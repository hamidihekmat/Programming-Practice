from threading import Thread
import requests

counter = 0


def image_downloader(image):
    global counter
    name = image.split('/')
    image = requests.get(image).content
    counter += 1
    with open('file{}.jpg'.format(counter), 'wb') as image_file:
        image_file.write(image)
        print('image downloaded')




image_1 = 'https://resize.hswstatic.com/w_907/gif/tesla-cat.jpg'
image_2 = 'https://images.unsplash.com/reserve/NnDHkyxLTFe7d5UZv9Bk_louvre.jpg?ixlib=rb-1.2.1&auto=format&fit=crop&w=1340&q=80'
image_list = [image_1, image_2]

for img in image_list:
    Thread(target=image_downloader, args=[img]).start()
