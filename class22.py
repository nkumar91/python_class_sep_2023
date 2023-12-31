from bs4 import BeautifulSoup
html_doc = 'web.html'
raw_html = open(html_doc).read()
soup = BeautifulSoup(raw_html, 'html.parser')
print(soup.prettify())



# print(soup.title.string)
# print(soup.a.string)
# print(soup.find_all('a'))

# for link in soup.find_all('a'):
#     print(link.get_text())


# x = soup.find(id="link2")

# print(x.get_text())

# x = soup.find(id="link2")

# print(type(x))

x = soup.find_all(class_='sis')
x[0].id = "jaan maro"
print(x[0].id)





