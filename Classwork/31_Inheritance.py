'''class Status:
    def _init_(self,caption,image=None,video=None):
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

gopal = Status("Hey I'm using whatsapp","Goodmrng.png")
gopal.see_status()
gopal.likes()
gopal.addmusic("Fear song")

arun = Status("Good Evening","coffee.png")
arun.see_status()
arun.likes()
arun.addmusic('My love is gone')'''


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

