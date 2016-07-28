# quicksand_tools
API access to QuickSand.io

Find reports by sha256:
-----------------------

Try https://repo.quicksand.io/ **sha256** .json

Search reports by any hash:
---------------------------

GET or POST https://www.quicksand.io/api.php

### Query Params:

query: Any md5, sha1, sha256 or sha512

key: API key - random data to md5

A successful result will be a redirect to the static json url.

A not found report will return json 'result' = 0.

### Example:

https://repo.quicksand.io/4b3611bf8747835f5dd4f51f73eba2d44f6513cffea87fa0ab25c074f8e9fc42.json


Upload file for analysis:
-------------------------
POST https://www.quicksand.io/upload.php

### Query Params:

file[]: File content

Limits
------

File uploads limited to approximately 12mb.
