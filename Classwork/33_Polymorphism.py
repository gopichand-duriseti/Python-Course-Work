#METHOD OVERRIDING(same method,same parameters,different behavior)
class normalUser:
    def playvideo(self,name):#class normalUser: #base/parent class
        print(f"{name} is playing video with: \n1.Normal Quality\n2.Ads Run\n3.No Backgound Playing\n4.Limited Videos download\n5.Music with ads\n")
    def likes(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def title(self):
        pass
    def description(self):
        pass
    def subscribe(self):
        pass

class premiumUser(normalUser):
    def playvideo(self,name):
        print(f"{name} is playing video with: \n1.High Quality\n2.No Ads\n3.Backgound Playing\n4.Download anything\n5.Music without ads")

gopi=normalUser()
gopal=premiumUser()
gopi.playvideo('gopi')
gopal.playvideo('gopal')