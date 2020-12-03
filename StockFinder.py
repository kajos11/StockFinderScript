#Script to find any stock which is not usually available
#also can be modified to buy any item during flash sale

import requests
import logging
import re
from playsound import playsound
from threading import Thread

#setting logging basic info
logging.basicConfig(level = logging.INFO, filename = 'findCards.log', filemode = 'a',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

#add product links here, few sites may block you temporarily!
urls=["https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518",
      "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3885-kr/p/N82E16814487520",
      "https://www.newegg.com/pny-geforce-rtx-3080-vcg308010tfxmpb/p/N82E16814133810",
      "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3885-kr/p/N82E16814487520",
      "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453",
      "https://www.bhphotovideo.com/c/product/1595780-REG/pny_technologies_vcg308010tfxmpb_geforce_rtx_3080_10gb.html",
      ]


#stock text to validate
outOfStockTextList = ["OUT OF STOCK","Notify When Available"]
inStockTextList = ["In Stock","Add to Cart"]

#function to play music when stock found.
def playFoundMusic():
   playsound("https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3")

#loop over infinite times!
while 1:
    #loop over all urls
    for i in range(len(urls)):
        x = re.search("https?://([A-Za-z_0-9.-]+).*", urls[i])
        r = requests.get(urls[i])
        res = r.text.encode("utf-8")
        #if status code not 200
        if(r.status_code != 200):
            logging.error ("ERROR! STATUS: "+str(r.status_code)+" ["+x.group(1)+"]"+urls[i])
        #check if stock is present    
        elif not(any(outOfStockText in res for outOfStockText in outOfStockTextList)):
            logging.info ("FOUND: ["+x.group(1)+"]"+urls[i])
            Thread(target=playFoundMusic).start()
        #stock not present
        else:
            logging.info ("NOT FOUND: ["+x.group(1)+"]"+urls[i])


