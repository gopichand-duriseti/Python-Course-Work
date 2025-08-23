from abc import ABC, abstractmethod
class Content(ABC): #It sets the rules to follow 
    @abstractmethod
    def upload(self):
        pass

class Photo(Content):
    def upload(self):
        print("Compressing photo...")
        print("Uploading photo...")
        print("Photo uploaded successfully!")

class Video(Content):
    def upload(self):
        print("Encoding video...")
        print("Uploading video...")
        print("Video uploaded successfully!")

class Reel(Content):
    def upload(self):
        print("Adding effects to reel...")
        print("Uploading reel...")
        print("Reel uploaded successfully!")
contents = [Photo(), Video(), Reel()]
Photo().upload()
print()
for content in contents:
    content.upload()
    print()