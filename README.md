# QuickSand.io API
<img src="https://quicksand.io/images/Quicksand/Icon_Colour/Quicksand-Icon-Colour.png" height="250"><img src="https://quicksand.io/images/quicksand.png" height="250">

API access to QuickSand.io. Python command line file uploader (support for password protected zip uploads), and command line report search.

Find reports by sha256:
-----------------------

Try https://repo.quicksand.io/ **sha256** .json

Search reports by any hash:
---------------------------

GET or POST https://www.quicksand.io/api.php

### Query Params:

query: Any md5, sha1, sha256, sha512 or sample ID

key: API key - random data to md5

A successful result will be a redirect to the static json url.

A not found report will return json 'result' = 0.

### Example:

https://www.quicksand.io/api.php?query=4b3611bf8747835f5dd4f51f73eba2d44f6513cffea87fa0ab25c074f8e9fc42&key=d96e8f982973b7a4117c5288b1d8d26a

redirects to: 

https://repo.quicksand.io/4b3611bf8747835f5dd4f51f73eba2d44f6513cffea87fa0ab25c074f8e9fc42.json


Upload file for analysis:
-------------------------
POST https://www.quicksand.io/upload.php

### Query Params:

file[]: File content

key: API key - random data to md5 - json output returned for any random key, otherwise html if ommited.

unzip: Password to unzip encrypted archive containing the sample (optional).

Poll for reports:
-----------------

GET or POST https://www.quicksand.io/api.php

This special query returns the next report starting at sample ID 1 through the current sample. Result = 0 on no more reports.

### Query Params:

query: next

key: API key - random data to md5 - used as a placeholder

A successful result will be a redirect to the static json url of the next report and save the report ID associated to your md5 key.

No more reports will return json 'result' = 0.


Limits
------

File uploads limited to approximately 12mb.


