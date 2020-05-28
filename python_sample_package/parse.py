from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()












'''from bs4 import BeautifulSoup
import requests

s=requests.get("http://coreyms.com").text
soup=BeautifulSoup(s,"lxml")
#print(soup)
#print(soup.prettify())
article=soup.find("article")
#print(article.prettify())
summary=article.find("div",class_="entry-content").p.text
#print(summary)

vid_src=article.find("iframe",class_="youtube-player")['src']
print(vid_src)
vid_id=vid_src.split("?")[0]
#vid_id=vid_src.split("/")[4]
print(vid_id)
vid_id1=vid_id.split("/")[4]
print(vid_id1)
yt_link=f"https://youtube.com/watch?v={vid_id1}"
print(yt_link)'''






'''soup=BeautifulSoup(s,"lxml")
print(soup.prettify())
header=soup.find(class_="entry_header")
k=header.h2.a.text
print(k)
article=soup.find("article")
#print(article.prettify())
headline=article.a.text
#print(headline)
te=article.find(class_="footer")
#print(te)
#print(te.a.txt)'''