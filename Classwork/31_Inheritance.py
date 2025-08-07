'''class Status:
    def __init__(self,caption,image=None,video=None):
        self.caption = caption
        self.image = image
        self.video = video
        self.videolength=30

    def see_status(self):
        if self.video:
            print(f"----{self.video}----\n{self.caption}")
        else:
            print(f"----{self.image}----\n'{self.caption}'")
class StatusV1(Status):
    def likes(self):
        print("Like")
    def addmusic(self,music):
        print(f"{music} Added")

gopal = StatusV1("Hey I'm using whatsapp","Goodmrng.png")
gopal.see_status()
gopal.likes()
gopal.addmusic("Fear song")

arun = StatusV1("Good Evening","coffee.png")
arun.see_status()
arun.likes()
arun.addmusic('My love is gone')
'''

#SINGLE INHERITANCE
class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is addded to your status')
gopi=Status()
gopi.uploadImage('selfie.png')

siddhu=StatusV1()
siddhu.uploadImage('Good Morning.png')
siddhu.addCaption('Hello Friends!!!!')

#HIERARCHICAL INHERITANCE(One Parent,Multiple Child)
class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is addded to your status')
class StatusV2(Status):
    def like(self):
        print(f'You can like status')
gopi=Status()
gopi.uploadImage('selfie.png')

siddhu=StatusV1()
siddhu.uploadImage('Good Morning.png')
siddhu.addCaption('Hello Friends!!!!')

manoj=StatusV2()
manoj.uploadImage("Coffee.png")
manoj.like()
#MULTIPLE INHERITANCE
class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is addded to your status')
class StatusV2(Status):
    def like(self):
        print(f'You can like status')
class StatusV3(StatusV1,StatusV2):
    def addmusic(self,music):
        self.music=music
        print(f"{self.music}... is added to your status")
class StatusV4(StatusV3): 
    def videolength(self,video):
        self.video=video
        print(f'{self.video} is uploaded to your status')

#ABOVE EXAMPLE CAN ALSO BE CALLED AS HYBRID INHERITANCE #It is a combination of two or more types of inheritance
#STATUS TO STATUSV1(SINGLE),STATUSV3(MULTIPLE),STATUSV3 TO STATUSV4(MULTILEVEL)

gopi=Status()
gopi.uploadImage('selfie.png')

siddhu=StatusV1()
siddhu.uploadImage('Good Morning.png')
siddhu.addCaption('Hello Friends!!!!')

manoj=StatusV2()
manoj.uploadImage("Coffee.png")
manoj.like()

mukesh=StatusV3()
mukesh.uploadImage('Metro.png')
mukesh.addCaption('Be Straight as an arrow')
mukesh.like()
mukesh.addmusic('Saiyaara.mp3')

manish=StatusV4()
manish.uploadImage('Sunrise.png')
manish.addCaption('Silence')
manish.like()
manish.addmusic('oohh manishi.mp3')
manish.videolength('Kalahasthi gadha.mp4')