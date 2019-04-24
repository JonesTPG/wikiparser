import requests
from database import Database


titlelist = []

# this is the amount of pages the workers will actually use, even though we fetch 500
# random pages from the API.
GLOBAL_PAGE_AMOUNT = 10


# global database connection for the single-threaded version

DATABASE_CON = Database(sdow_database='./sdow.sqlite', searches_database='./result.sqlite')

# since the sqlite3 as a database engine is limited, the multi-threaded version will use different copies of the database

THREAD_1_DATABASE_CON = Database(sdow_database='./sdow.sqlite', searches_database='./result.sqlite')
THREAD_2_DATABASE_CON = Database(sdow_database='./sdow2.sqlite', searches_database='./result.sqlite')
THREAD_3_DATABASE_CON = Database(sdow_database='./sdow3.sqlite', searches_database='./result.sqlite')
THREAD_4_DATABASE_CON = Database(sdow_database='./sdow4.sqlite', searches_database='./result.sqlite')




def main():

    #lets get 500 random pages from wikipedia web api
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "500",
        "rnnamespace": "0"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    rows = DATA.get("query").get("random")

    for row in rows:
        title = row.get('title')
        titlelist.append(title)

