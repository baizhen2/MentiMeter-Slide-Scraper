import requests
import json_parser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

def main():
    id = input("Enter MentiMeter code: ")
    mentiURL = getMentiURL(id)
    json = requests.get(mentiURL, headers=headers).json()

    jsonParser = json_parser.JsonParser(json)
    images = jsonParser.getImages()



def getMentiURL(id):
    return "https://www.menti.com/core/vote-ids/" + id.replace(" ", "") + "/series"

if __name__=="__main__":
    main()