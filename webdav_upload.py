# v0.1 from https://github.com/thorbenegberts/webdav-upload-script/

import easywebdav
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
	webdav.upload(fileFrom, fileTo)