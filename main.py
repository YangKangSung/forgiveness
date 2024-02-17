import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

base_url="https://torrenttop88.com"
def extract_links(keyword):
  url = f"{base_url}/search/index?keywords={keyword}"
  response = requests.get(url)
  response.raise_for_status()
  soup = BeautifulSoup(response.content, "html.parser")

  items = soup.find_all("div", class_="py-4 flex flex-row border-b topic-item")
  links = []
  for item in items:
    title = item.find("a")["title"]
    href = item.find("a")["href"]
    if title and href:
        links.append({'title': title, 'href': href})
  return links

def extract_magnet_links(href):
	url = f"{base_url}{href}"
	print(f"{url=}")

	response = requests.get(url)
	response.raise_for_status()

	soup = BeautifulSoup(response.content, "html.parser")
	items = soup.find_all("div", class_="p-3")
	print(items)

encoded_keyword = quote(input("검색어를 입력하세요: "))
links = extract_links(encoded_keyword)
print(f"총 {len(links)}개의 링크를 찾았습니다.")
for link in links:
  print(link)

first_item = links[0] if links else None
print(f"{first_item=}")

link = extract_magnet_links(first_item['href'])


