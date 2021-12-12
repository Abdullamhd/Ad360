


url = "https://addata.gov.ae/search/type/dataset"


# download the page
import requests
from bs4 import BeautifulSoup

# save the page in variable
page = requests.get(url)

