import easywebdav
import glob

class WebDavTools:
    def __init__(self):
        self.webDav = None

    # Has to be called before interacting with the server
    def connect(self, url, username, password):
        self.webDav = easywebdav.connect(url, username=username, password=password)

    # Upload files or directories. If source is an directory, target has to be an directory, too.
    def upload(self, source, target):
        self.checkConnection()
        if not source:
            raise Exception("Source must be set")
        if not target:
            raise Exception("Target must be set")


        # If there are more than one file, files will be extracted into a folder. The path will
        # be created, if it doesn't exist. If the path is in reality a file, there will be an error.
        # An target directory has to end with an "/" per definition. This should be pointed out
        # clearly in the documentation.

        files = glob.glob(source)

        self.createPath(target)

        # Directory?
        if target.endswith('/'):
            # Is directory
            for file in files:
                # print "uploading " + file + " to " + target + "/" + self.extractFilename(file)
                self.webDav.upload(file, target + "/" + self.extractFilename(file))
        else:
            # No directory, will be handles als single file (even if the pattern would contain multiple files)
            if len(files):
                self.webDav.upload(files[0], target)

    def checkConnection(self):
        if self.webDav == None:
            raise Exception("You must connect first.")

    def extractFilename(self, filePath):
        splittedFilePath = filePath.split('/')
        if len(splittedFilePath) > 1:
            return splittedFilePath[len(splittedFilePath) - 1]
        else:
            return filePath

    def createPath(self, filePath):
        self.checkConnection()
        if not self.webDav.exists(filePath):
            self.webDav.mkdirs(filePath)