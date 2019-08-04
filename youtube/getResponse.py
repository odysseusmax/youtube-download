import pafy, traceback

class GetDetails:
    
    def __init__(self, url):
        
        self.url = url
        self.error=False
        self.error_msg=None
        try:
            self.vid = pafy.new(self.url)
        except Exception as e:
            traceback.print_exc()
            self.error=True
            self.error_msg=str(e)
    
    async def details(self):
        
        try:
            self.thumb = self.vid.bigthumbhd or self.vid.bigthumb or self.vid.thumb
            self.category = self.vid.category
            self.description = self.vid.description
            self.title = self.vid.title
            self.userName = self.vid.username
            self.published = self.vid.published
        except Exception as e:
            traceback.print_exc()
            self.error=True
            self.error_msg=str(e)
    
    async def streams(self):
        
        self.streams = []
        
        try:
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
        except Exception as e:
            traceback.print_exc()
            self.error=True
            self.error_msg=str(e)
    
    async def process_output(self):
        
        
        return dict(status=True,
                    msg="ok",
                    data=dict(title=self.title,
                            description=self.description,
                            thumb=self.thumb,
                            category=self.category,
                            userName=self.userName,
                            published=self.published,
                            streams=self.streams
                    )
                )
    
    async def get(self):
        
        if(self.error):
            response = dict(
                status=False,
                msg=self.error_msg,
                data={}
                )
        else:
            await self.details()
            await self.streams()
            if(self.error):
                response = dict(
                    status=False,
                    msg=self.error_msg,
                    data={}
                    )
            else:
                response = await self.process_output()
        return response
        
        
    
