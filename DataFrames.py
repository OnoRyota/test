import pandas #pandasをインポート
import pprint

import requests
from bs4 import BeautifulSoup

#取得したいページのurlを入力(url)
url = 'https://weather.yahoo.co.jp/weather/jp/44/8320/44214.html'

#urlを読み取る
fetched_dataframes = pandas.io.html.read_html(url)

#to_json関数で文字列をjsonに変換し，checkitup.jsonで保存
#[4]で明日の天気,[5]で一週間の天気
fetched_dataframes[4].to_json('check.json',force_ascii=False)

#プリントしたい場合
ret = fetched_dataframes[4].to_json(force_ascii=False)
pprint.pprint(ret)
