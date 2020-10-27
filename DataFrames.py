import pandas #pandasをインポート
import pprint

#取得したいページのurlを入力
url = 'https://www.jma.go.jp/jp/amedas_h/today-83216.html?areaCode=000&groupCode=59'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url)

#to_json関数で文字列をjsonに変換し，OitaAmeme.jsonで保存
fetched_daraframes[4].to_json('OitaNoAme.json',force_ascii=False)

#プリントしたい場合
ret = fetched_daraframes[4].to_json(force_ascii=False)
pprint.pprint(ret)