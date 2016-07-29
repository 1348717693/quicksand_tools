import requests
import argparse

url = "https://www.quicksand.io/api.php"

#handle command lines
parser = argparse.ArgumentParser()
parser.add_argument("query", help="Hash to find md5,sha1,sha256,sha512")
parser.add_argument("-k", "--key", help="Optional API Key", default="0000000000000000000000000000000a")
args = parser.parse_args()


values = {'key': args.key, 'query': args.query}
r = requests.post(url, data=values)
print r.text
