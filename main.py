import requests
from bs4 import BeautifulSoup

def extract_links(keyword):
  """
  토렌트 검색 결과에서 링크 추출

  Args:
    keyword: 검색어

  Returns:
    링크 목록
  """

  # URL 생성
  url = f"https://torrenttop88.com/search/index?keywords={keyword}"

  # HTML 응답 가져오기
  response = requests.get(url)
  response.raise_for_status()

  # BeautifulSoup 객체 생성
  soup = BeautifulSoup(response.content, "html.parser")

  # 토렌트 항목 목록 추출
  items = soup.find_all("div", class_="py-4 flex flex-row border-b topic-item")

  # 각 항목에서 href 속성 추출
  links = []
  for item in items:
    title = item.find("a")["title"]
    href = item.find("a")["href"]
    if title and href:
        links.append({'title': title, 'href': href})
  return links

# 검색어 입력
keyword = input("검색어를 입력하세요: ")

# 링크 추출
links = extract_links(keyword)

# 결과 출력
print(f"총 {len(links)}개의 링크를 찾았습니다.")
for link in links:
  print(link)
