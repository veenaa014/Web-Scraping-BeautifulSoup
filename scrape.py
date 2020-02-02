from bs4 import BeautifulSoup
import requests
import csv

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify()) #prettify gives indent to the file

match = soup.title.text #title grabs only the first title tag
# print(match)

match = soup.div #this grabs the first div tag
# print(match)

#using find method for selective search
match = soup.find('div', class_='footer')
# print(match)

article = soup.find('div', class_='article') # find returns the first tag that matches this argument
# print(article)

headline = article.h2.a.text
# print(headline)

summary = article.p.text
# print(summary)

# for article in soup.find_all('div', class_='article'): #find_all returns a list of all tags that matches this argument
#     headline = article.h2.a.text
#     print(headline)
#
#     summary = article.p.text
#     print(summary)
#     print()


source = requests.get('http://startupnextdoor.com').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('scapedcsv.csv', 'w')
# print(soup.prettify())
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary'])

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print(headline)
    # summary = article.p.text
    # print(summary)
    summary = article.find('section', class_ = 'post-excerpt' ).p.text
    print(summary)
    print()
    csv_writer.writerow([headline, summary])

csv_file.close()
