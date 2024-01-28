from bs4 import BeautifulSoup
import requests
try:
    #input_url = input("Enter Url\n")
    input_url = "https://goldsgym.in/personal-trainingour-programs.html"
    web_html = requests.get(url = input_url, stream=True) 
    raw_html = web_html.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    print(soup.prettify())
    all_deals = soup.find_all(class_='fusion-text')
    for i in all_deals[0].find_all("li"):
        print(i.get_text())
except Exception:
    print("Exception Occur")

