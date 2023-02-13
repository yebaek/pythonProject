'''

'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
# param = {'code': 10016}
response = requests.get(url)
html = response.text
print(response.text)




# soup = BeautifulSoup(html, 'html.parser')

# review_list = soup.find_all('div', class_='score_reple')

# for review in review_list:
#    print(review.find('p').text.strip())