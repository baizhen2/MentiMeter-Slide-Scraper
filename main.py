import requests
import json_parser
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

def main():
    id = input("Enter MentiMeter code: ")
    mentiURL = getMentiURL(id)
    json = requests.get(mentiURL, headers=headers).json()

    #Error handling
    if response.status_code == 404:
        print("Possible expired MentiMeter key")
        return
    elif response.status_code != 200:
        print("Unknown Error")
        return
    
    json = response.json()
    jsonParser = json_parser.JsonParser(json)
    images = jsonParser.getImages()

    os.makedirs(r'../menti_slides/' + jsonParser.getPresentationName())


def getMentiURL(id):
    return "https://www.menti.com/core/vote-ids/" + id.replace(" ", "") + "/series"

if __name__=="__main__":
    newpath = r'../menti_slides' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
    main()