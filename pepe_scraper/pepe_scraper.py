from bs4 import *
import requests
# TODO
# MAKE PEPE SCRAPER ASYNCHRONOUS

pepe_req = requests.get("https://www.memeatlas.com/pepe-memes.html")
soup = BeautifulSoup(pepe_req.text, "lxml")

links_png=[]
links_jpg =[]
links_gif =[]

x = soup.select('a')

for img in x:
    if img['href'].endswith('.png'):
        links_png.append('https://www.memeatlas.com/'+ img["href"])
    elif  img['href'].endswith('.jpg'):
        links_jpg.append('https://www.memeatlas.com/'+ img["href"])
    elif  img['href'].endswith('.gif'):
        links_gif.append('https://www.memeatlas.com/'+ img["href"])
for index, img_link in enumerate(links_png):
    if img_link[-4:] == '.png':
        img_data = requests.get(img_link).content
        with open("pepe_photos/"+str(index+1) + 'png' + '.png' ,'wb+') as f:
            f.write(img_data)
for index, img_link in enumerate(links_gif):
    if img_link[-4:] == '.gif':
        img_data = requests.get(img_link).content
        with open("pepe_photos/"+str(index+1) + 'gif' + '.gif' ,'wb+') as f:
            f.write(img_data)
for index, img_link in enumerate(links_jpg):
    if img_link[-4:] == '.jpg':
        img_data = requests.get(img_link).content
        with open("pepe_photos/"+str(index+1) + 'jpg' + '.jpg' ,'wb+') as f:
            f.write(img_data)
    
    
        

    
    


