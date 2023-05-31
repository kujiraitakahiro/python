import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# コマンドライン引数からテキストファイルと保存ファイルの名前を取得する
input_file = sys.argv[1]
output_file = sys.argv[2]

# テキストファイルからデータを読み込む
with open(input_file, "r") as f:
    words = f.read().splitlines()

# ワードクラウドを作成する
# 日本語のフォントのパスを指定する
# 単語の重複表示は無効化する
wc = WordCloud(background_color="white",
               font_path="/usr/share/fonts/meiryo/meiryo.ttc",
               width=1000, height=750,
               collocations=False)

wordcloud = wc.generate(" ".join(words))

# ワードクラウドを表示する
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# ワードクラウドをファイルに保存する
wordcloud.to_file(output_file)

