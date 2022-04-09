import requests
import json_parser
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

def main():
    id = input("Enter MentiMeter code: ")
    mentiURL = getMentiURL(id)
    response = requests.get(mentiURL, headers=headers)

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

    dstFolderName = makeFolders(jsonParser.getPresentationName())

    for image in images:
        image.downloadImage(dstFolderName + "/")


def getMentiURL(id):
    return "https://www.menti.com/core/vote-ids/" + id.replace(" ", "") + "/series"

def makeFolders(presentationName):
    newpath = r'../menti_slides/' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    dstFolder = newpath + presentationName
    os.makedirs(dstFolder)

    return dstFolder


if __name__=="__main__":
    main()