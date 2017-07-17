import requests
import urllib.request
from bs4 import BeautifulSoup


def make_soup(arg_url):
    source_code = requests.get(arg_url)
    source_text = source_code.text
    return BeautifulSoup(source_text, 'lxml')


def download_images(url):
    soup = make_soup(url)
    index = 0
    for img in soup.findAll('img'):
        photo_url = url + img.get('src') if img.get('src')[:1] is '/' else img.get('src')
        filename = img.get('alt') if len(img.get('alt')) > 0 else "unknown_img" + str(index)
        img_file = open(filename + '.jpeg', 'wb')
        img_file.write(urllib.request.urlopen(photo_url).read())
        index += 1
    img_file.close()


def main():
    download_images('http://www.yahoo.com')


if __name__ == '__main__':
    main()
