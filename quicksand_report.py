import requests

url = "https://www.quicksand.io/api.php"
values = {'key': '60bb2e16f59a8e7c6b51101a79b34cd9', 'query': '42d087ac77d8bab5c418ccf0828698db4656e539d60174aa2ea5b5a802f9c4fa'}

r = requests.post(url, data=values)
print r.text
