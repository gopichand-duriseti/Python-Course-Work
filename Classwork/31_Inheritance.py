class Status:
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

gopal = StatusV1("Hey I'm using whatsapp","Goodmrng.png")
gopal.see_status()
gopal.likes()
gopal.addmusic("Fear song")

arun = StatusV1("Good Evening","coffee.png")
arun.see_status()
arun.likes()
arun.addmusic('My love is gone')