import pafy

class GetDetails:
    
    def __init__(self, url):
        
        self.url = url
        print(self.url)
        self.vid = pafy.new(self.url)
    
    async def details(self):
        
        self.thumb = self.vid.bigthumbhd or self.vid.bigthumb or self.vid.thumb
        self.category = self.vid.category
        self.description = self.vid.description
        self.title = self.vid.title
        self.userName = self.vid.username
        self.published = self.vid.published
    
    async def streams(self):
        
        self.streams = []
        
        for stream in self.vid.allstreams:
            
            self.streams.append(
                dict(url = stream.url,
                     bitRate = stream.bitrate,
                     mediaType = stream.mediatype,
                     quality = stream.quality,
                     fileSize = stream.get_filesize(),
                     extension = stream.extension
                )
            )
    
    async def process_output(self):
        
        return dict(title=self.title,
                    description=self.description,
                    thumb=self.thumb,
                    category=self.category,
                    userName=self.userName,
                    published=self.published,
                    streams=self.streams
                )
    
    async def get(self):
        
        await self.details()
        await self.streams()
        return await self.process_output()
        
        
    
