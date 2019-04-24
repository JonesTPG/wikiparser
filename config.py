import requests

titlelist = []



# this is the amount of pages the workers will actually use, even though we fetch 500
# random pages from the API.
GLOBAL_PAGE_AMOUNT = 20

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


