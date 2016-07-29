import requests

url = "https://www.quicksand.io/upload.php"
files = {'file[]': open('file.doc', 'rb')}
values = {'key': '60bb2e16f59a8e7c6b51101a79b34cd9'}

r = requests.post(url, files=files, data=values)
print r.text
