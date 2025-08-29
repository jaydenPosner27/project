import requests
import string
import json

API_KEY = "ad1178859688fbab3634d9904e6c3273"

def normalize(title):
    normalized = str.maketrans('', '', string.punctuation + " ")
    return title.translate(normalized).lower()



def getSongs(artist, album):
    url = "https://ws.audioscrobbler.com/2.0/"
    param = {"method":"album.getinfo", "api_key":API_KEY, "artist":artist, "album":album, "format":"json"}
    data = requests.get(url, params=param).json()
    songData = data["album"]["tracks"]["track"]
    retList = []
    for song in songData:
        retList.append(song["name"])
    return retList


def compare(allSongs, rankedSongs):
    for songs in allSongs:
        min = 0
        category = input("Would you say " + songs + " is great, mid, or bad? ").lower()
        while category not in rankedSongs:
            category = input("enter a valid answer ").lower()
        max = len(rankedSongs[category])-1
        if max == -1:
            rankedSongs[category].append(songs)
            continue
        i=int(max/2)
        while(True):
            choice = input(songs + " or " + rankedSongs[category][i] + "? ")
            if normalize(choice) == normalize(songs):
                max = i -1
                #print(str(min) + " " + str(max) + " " + str(i))       
            elif normalize(choice) == normalize(rankedSongs[category][i]):
                min = i + 1
                #print(str(min) + " " + str(max) + " " + str(i))
            else:
                print("enter a valid answer")
            if min>max:
              rankedSongs[category].insert(min,songs)
              break
            i = int((min+max)/2)
    print(rankedSongs[category])
    


#def sort()
    

artistName = input("You will enter the name of a music artist, and one of their albums, then rank the songs. First, enter in the name of the artist whose album you want to rank\n")
albumName=input("Now enter the name of the album\n")
rankedList = {
    "great":[], "mid":[], "bad":[]
}
songList = getSongs(artistName, albumName)
compare(songList,rankedList)

