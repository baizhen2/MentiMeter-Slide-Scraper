# MentiMeter Slide Scraper

A request-based image/slide grabber for MentiMeter

- Currently only supports images on MentiMeter slides 
- Can support text as well, looking for formatting ideas


## Windows/MacOS Installation

 - Click Code > Download ZIP > Create a folder on your PC > Extract All Files to that folder

 - Open command prompt/terminal in your respective OS

We are making use of docker to run the application 

 - You will need to download docker desktop

 - Change directory to the folder of extracted files ex. ```cd C:\Users\Baizhen\Desktop\MentiMeter-Slide-Scraper```

 - Your currently directory should now contain the python and docker files, if it doesn't you are in the wrong directory
 
**Building/Using the Application** 

 - If you are in the right directory you can now run ```docker-compose build```
 - On MacOS/Linux you might encounter a permission error with docker.sock, in this case run ```sudo docker-compose build```, this will prompt for your password
 - If the above commands are successfully you will see docker building the image
<img width="659" alt="build" src="https://user-images.githubusercontent.com/62679957/162652226-2c89d119-6980-45d0-83de-7dd72afc40ae.png">
 - You can now run the application using ```docker-compose run app``` or for MacOS/Linux ```sudo docker-compose run app```
<img width="611" alt="run-app" src="https://user-images.githubusercontent.com/62679957/162652274-4e76f4da-ee56-4d0c-96df-98dc5c68f428.png">
 - The final result is the application prompting for the MentiMeter key, which is the same code your teacher/professor puts up for you to join the presentation
 - The images will then be downloaded to a newly created folder called ```menti_slides```
 - If you need to rerun the program use ```docker-compose run app``` or for MacOS/Linux ```sudo docker-compose run app``` as you won't need to rebuild it

***Images are just normal files without a type!?!***
 - Some images from the slides might be a .jpeg type, which in some cases Windows cannot recognize 
 - For these files you will need to convert them to a .jpg type, which can be done using a converter found online
 - Google ```jpeg to jpg converter``` and you will find tons of them

## Improvements 
More automation!!!

### 1. Complete Presentation
 - Currently only the images are being pulled from the presentation. Its more of an formatting/design problem of how text should be presented. One big text file? Multiple text files?
 - If you have an idea please submit a pull request!
 
### 2. Auto Convert JPEG
 - This will probably be the next feature if there is enough demand from me or others. 

## Final Thoughts 
This was a quick weekend project to improve my class experience. My professor doesn't upload his powerpoints but he does use MentiMeter so I can grab the presentation from there. Just my solution to a small problem which improves my daily life.

## License
[MIT](https://choosealicense.com/licenses/mit/)
