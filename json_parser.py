import image

class JsonParser:

    def __init__(self, jsonObject):
        self.json = jsonObject

    def getImages(self):
        images = []
        slideCounter = 1

        for q in self.json["questions"]:
            if (q["question_image_url"] != None):
                newImage = image.Image(q["question_image_url"], "slide" + str(slideCounter) + "-" + q["slug"])
                slideCounter += 1
                images.append(newImage)
        return images
    
    def getPresentationName(self):
        return self.json["name"]