SEARCH_KEY = "AIzaSyCiUEa-IoeEGRcecroTnEiJZzgrfur2Kj0"
SEARCH_ID = "773f9d4337d4d4174"
COUNTRY = "in"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *