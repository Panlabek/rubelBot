from bs4 import *
import requests
import aiohttp
import time
import asyncio

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
# start = time.time()
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for index, img_link in enumerate(links_png):
            if img_link[-4:] == '.png':
                extension = ".png"
                task = asyncio.ensure_future(getPepe(session, img_link, index, extension))
                tasks.append(task)
        for index, img_link in enumerate(links_gif):
            if img_link[-4:] == '.gif':
                extension = ".gif"
                task = asyncio.ensure_future(getPepe(session, img_link, index, extension))
                tasks.append(task)
        for index, img_link in enumerate(links_jpg):
            if img_link[-4:] == '.jpg':
                extension = ".jpg"
                task = asyncio.ensure_future(getPepe(session, img_link, index, extension))
                tasks.append(task)
        await asyncio.gather(*tasks)

async def getPepe(session, url, index, extension):
    async with session.get(url) as response:
        img = await response.read()
        with open(f"pepePhotos/{str(index+1)}{extension[1:]}{extension}", "wb+") as f:
            f.write(img)
asyncio.run(main())
# print(f"Pepe scraping took {time.time() - start}")
        
    
    


