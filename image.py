import shutil
import requests

class Image:

    def __init__(self, imageURL, name):
        self.imageURL = imageURL
        self.imageName = name

    def cleanImageUrl(self):
        self.imageUrl = self.imageURL.split("?auto=compress")[0]
    
    def downloadImage(self, dstFolder):
        self.cleanImageUrl()

        r = requests.get(self.imageURL, stream = True)

        if r.status_code == 200:
            r.raw.decode_content = True
            
            with open(dstFolder + self.imageName,'wb') as f:
                shutil.copyfileobj(r.raw, f)