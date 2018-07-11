import os
import requests
import urllib.request
from bs4 import BeautifulSoup

def download_lyrics(site, st):
    url = site
    resp = requests.get(url)
    resp.encoding = 'big5'
    soup = BeautifulSoup(resp.text, 'html.parser')
    songs = soup.find_all('a')
    for song in songs:
        s = song.get('href')
        try:
            if ".mid" in s and ".midi" not in s:
                print(s)
                urllib.request.urlretrieve(s,"midi/" + st + "/" + song.get_text().strip() + ".mid")
        except:
            pass

URL = 'http://cometrain03.tripod.com/midifiles/Bans_and_Groups.htm'
RESP = requests.get(URL)
RESP.encoding = 'big5'
SOUP = BeautifulSoup(RESP.text, 'html.parser')
singers = SOUP.find_all('a')

for singer in singers[112:]:
    if singer.find('font'): 
        st = singer.find('font').get_text().strip()
        if st[0] >= 'A' and st[0] <= 'Z': 
            pass
        else:
            print(st)
            os.mkdir("midi/" + st)
            download_lyrics(singer.get('href'), st)

    else:
        st = singer.get_text().strip()
        if st[0] >= 'A' and st[0] <= 'Z': 
            pass
        else:
            print(st)
            os.mkdir("midi/" + st)
            download_lyrics(singer.get('href'), st)
        
