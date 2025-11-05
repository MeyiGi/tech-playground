import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
url = "https://gazi.edu.tr/view/announcement-list?id={}&type=1&SearchString=&dates=&date="

res = []

for i in range(1, 5):
    url.format(i)
    response = requests.get(url.format(i))
    soup = BeautifulSoup(response.content, "html.parser")
    announcements = soup.select(".row.subpage-ann-single.flex-nowrap")
    for announcement in announcements:
        day = announcement.select_one(".ann-day").get_text(strip=True)
        month = announcement.select_one(".ann-month").get_text(strip=True)
        year = announcement.select_one(".ann-year").get_text(strip=True)
        date = f"{day} {month} {year}"
        link = announcement.select_one(".subpage-ann-link > a").get("href")
        post_url = urljoin("https://gazi.edu.tr", link)
        title = announcement.select_one(".subpage-ann-link").get_text(strip=True)

        response = requests.get(post_url)
        post_soup = BeautifulSoup(response.content, "html.parser")
        content_div = "\n".join(item.get_text(strip=True) for item in post_soup.select(".subpage-content-txt p"))

        res.append({"date": date, "title": title, "language" : "tr-TR", "link": post_url, "content": content_div})
print(res)
print(len(res))