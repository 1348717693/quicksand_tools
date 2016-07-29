import requests
import argparse

url = "https://www.quicksand.io/upload.php"

#handle command lines
parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to upload for analysis")
parser.add_argument("-k", "--key", help="Optional API Key", default="0000000000000000000000000000000a")
parser.add_argument("-p", "--password", help="Optional Unzip Password")
args = parser.parse_args()


files = {'file[]': open(args.file, 'rb')}
values = {'key': args.key}
if args.password:
  values['unzip'] = args.password

r = requests.post(url, files=files, data=values)
print r.text
