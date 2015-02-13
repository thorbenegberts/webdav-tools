# WebDav Tools

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
  File                 Multiple files devided by a colon from:to

optional arguments:
  -h, --help           show this help message and exit
  --url URL            The URL.
  --username USERNAME  The username.
  --password PASSWORD  The password.
```

**Example:**

Example usage for uploading two different files. You can specifiy as many files as you want. Note that you must define your local file and your desired remote file devided by a colon:

```
python webdav_upload.py --url=my.domain.com --username=myusername --password=mypassword /my/local/file/from.txt:/my/remote/file/to.txt /my/other/local/file/from.txt:/my/other/remote/file/to.txt
```
