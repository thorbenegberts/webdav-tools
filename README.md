# WebDav Upload Script

A simple python script for uploading multiple files to a WebDav server.

# Usage

## Setup

Install the (easywebdav)[https://github.com/amnong/easywebdav] gem:

```
easy_install easywebdav
```

## Usage

Output of `python webdav_upload.py --help`:

```
usage: webdav_upload.py [-h] --url URL [--username USERNAME]
                        [--password PASSWORD]
                        File [File ...]

WebDav upload processing.

positional arguments:
  File                 Multiple files devided by a colon from:to

optional arguments:
  -h, --help           show this help message and exit
  --url URL            The URL.
  --username USERNAME  The username.
  --password PASSWORD  The password.
```

## Example

Example usage for uploading two different files. You can specifiy as many files as you want. Note that you must define your local file and your desired remote file devided by a colon:

```
python webdav_upload.py --url=my.domain.com --username=myusername --password=mypassword /my/local/file/from.txt:/my/remote/file/to.txt /my/other/local/file/from.txt:/my/other/remote/file/to.txt
```
