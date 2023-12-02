import requests
from bs4 import BeautifulSoup
import time

stock = ["5347","5009"] # 你要爬的股票

for i in range(len(stock)):
  stockid = stock[i] # 0 -> 1
  url = 'https://tw.stock.yahoo.com/quote/'+ stockid +'.TW' # 網址
  r = requests.get(url) # 爬 HTML
  soup = BeautifulSoup(r.text, 'html.parser') # 解析 HTML
  # 根據 tag 和 class 取得股價
  price = soup.find('span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)', 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)', 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])
  # 假如沒有爬到 (例如是上櫃)
  if price == None:
    url = 'https://tw.stock.yahoo.com/quote/'+ stockid +'.TWO' # 上櫃網址規則
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)', 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)', 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])
  price = price.getText()

  # 回傳的訊息
  message = '股票' + stockid + '的即時價格為: ' + price
  # bot token
  token = '6674095910:AAH7Jd4nlQaJyEqXEObh_0vZLqen12oT__U'
  # 使用者 id
  chat_id = '5740033148'
  # 發送訊息
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url)
  time.sleep(3)
