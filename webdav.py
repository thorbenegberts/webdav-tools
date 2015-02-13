import easywebdav

class WebDav:
    def connect(self, url, username, password):
        self.webdav = easywebdav.connect(url, username=username, password=password)
    def uploadFile(fromFile, toFile):


