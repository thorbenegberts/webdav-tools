# v0.2 of https://github.com/thorbenegberts/webdav-upload-script/

import argparse

parser = argparse.ArgumentParser(description='WebDav upload processing.')

# List of files (required)
parser.add_argument('files', metavar='File', type=str, nargs='+', help='Multiple files devided by a colon from:to')

# The url (required)
parser.add_argument('--url', dest='url', help='The URL.', required=True)

# Username (optional)
parser.add_argument('--username', dest='username', help='The username.')

# Password (optional)
parser.add_argument('--password', dest='password', help='The password.')

# Parse all arguments. Will be available in the "args" namespace
args = parser.parse_args()

# Connect to WebDav with given credentials
webdav = easywebdav.connect(args.url, username=args.username, password=args.password)

# Upload files
for fileFromTo in args.files:
	# Files have to be devided by ":", e.g. "/my/local/file/from.txt:/my/remote/file/to.txt"
	fileSplitted = fileFromTo.split(':')
	if len(fileSplitted) != 2:
		raise Exception("Invalid file argument!")
	fileFrom = fileSplitted[0]
	fileTo = fileSplitted[1]

    # TODO fileFrom ein verzeichnis ist, dann darf fileTo keine einzeldatei sein, sondern ein verzeichnis. für
    # fileTo muss dann jeweils der dateiname von fileFrom übernommen werden, nachdem der ordner-
    # inhatl ausgelesen worden ist. also in der iteration

    # if isDirectory fileForm:
        # raise error if fileTo is not a directory
        # for each file:
            # toFile = toFile (directory) + filename (without directory)
            # upload toFile
    # else:
        # (default)
	webdav.upload(fileFrom, fileTo)

def upload(fromFile, toFile)
