# https://www.menti.com/core/vote-ids/9017332/series

import json
import json
import image

class JsonParser:

    def __init__(self, jsonObject):
        self.json = jsonObject

    def getImages(self):
        images = []
        slideCounter = 1

        for q in self.json["questions"]:
            if (q["question_image_url"] != None):
                newImage = image.Image(q["question_image_url"], q["slug"] + "-slide" + str(slideCounter))
                slideCounter += 1
                images.append(newImage)
        return images
    
