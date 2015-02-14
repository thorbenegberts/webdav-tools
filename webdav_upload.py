import argparse
import webdavtools

parser = argparse.ArgumentParser(description='WebDav upload processing.')

# List of files (required)
parser.add_argument(    'files',
                        metavar='File',
                        type=str,
                        nargs='+',
                        help='Multiple files, source and target divided by a colon '
                             'from:to. Directories have to end with a slash. File '
                             'patterns are allowed. Example: ~/Desktop/test/*.txt:/test/ '
                             '(will copy all txt-files from folder ~/Desktop/test/ to '
                             '/test/ on the WebDav server.')

# The url (required)
parser.add_argument(    '--url',
                        dest='url',
                        help='The URL.',
                        required=True)

# Username (optional)
parser.add_argument(    '--username',
                        dest='username',
                        help='The username.')

# Password (optional)
parser.add_argument(    '--password',
                        dest='password',
                        help='The password.')

# Parse all arguments. Will be available in the "args" namespace
args = parser.parse_args()

# Connect to WebDav with given credentials
webDavTools = webdavtools.WebDavTools()
webDavTools.connect(args.url, args.username, args.password)

# Upload files
for sourceAndTarget in args.files:
    # Files have to be devided by ":", e.g. "/my/local/file/from.txt:/my/remote/file/to.txt"
    sourceAndTargetSplitted = sourceAndTarget.split(':')

    if len(sourceAndTargetSplitted) != 2:
        raise Exception("Invalid file argument!")

    source = sourceAndTargetSplitted[0]
    target = sourceAndTargetSplitted[1]

    webDavTools.upload(source, target)