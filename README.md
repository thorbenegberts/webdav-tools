# WebDav Tools for Python

A collection of handy Python scripts that makes working with WebDav less painful. This project is built upon the [easywebdav](https://github.com/amnong/easywebdav) client for Python. The client itself is great, but I always had to write the same boilerplate code.

# Usage

## Setup

Install the [easywebdav](https://github.com/amnong/easywebdav) Client for Python:

```
easy_install easywebdav
```

## Usage

### Upload files or directories

Output of `python webdav_upload.py --help`:

```
usage: webdav_upload.py [-h] --url URL [--username USERNAME]
                        [--password PASSWORD]
                        File [File ...]

WebDav upload processing.

positional arguments:
  File                 Multiple files, source and target divided by a colon
                       from:to. Directories have to end with a slash. File
                       patterns are allowed. Example:
                       ~/Desktop/test/*.txt:/test/ (will copy all txt-files
                       from folder ~/Desktop/test/ to /test/ on the WebDav
                       server.

optional arguments:
  -h, --help           show this help message and exit
  --url URL            The URL.
  --username USERNAME  The username.
  --password PASSWORD  The password.
```

**Example:**

Example usage for uploading files. You can add as many file arguments as you want. Note that you must define your local file and your desired remote file devided by a colon:

```
python webdav_upload.py --url=my.domain.com --username=myusername --password=mypassword /my/local/files/*.txt:/my/remote/files/ /my/other/local/file/from.txt:/my/other/remote/file/to.txt
```

This will upload all `.txt` files from `/my/local/files/` to `/my/remote/files/` and the single file `/my/other/local/file/from.txt` to `/my/other/remote/file/to.txt` on the server.
