
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

import csv
import os

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
CSV_PATH ="CharacterList.csv"

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    if(os.path.exists(CSV_PATH)):
        with open(CSV_PATH) as csv_file:
            reader = csv.reader(csv_file)
            source.extend(list(reader)[0])
        
    if(word in source):
        print(f"{word}が見つかりました")
    else:   
        print(f"{word}が見つかりませんでした")
        source.append(word)

    with open(CSV_PATH, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(source)
        
if __name__ == "__main__":
    search()
