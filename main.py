import requests
from bs4 import BeautifulSoup as bs 

manga_name = input('input Manga name:')
url = 'https://www.mangahere.cc/manga/onepunch_man/' +manga_name
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'class' : 'detail-info-cover-img'})['src']
print(profile_image)