import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# コマンドライン引数からテキストファイルと保存ファイルの名前を取得する
input_file = sys.argv[1]
output_file = sys.argv[2]

# テキストファイルからデータを読み込む
with open(input_file, "r") as f:
    words = f.read().splitlines()

# ハート形のマスクを読み込む
mask = np.array(Image.open("heart_mask.png"))

# ワードクラウドを作成する
# 日本語のフォントのパスを指定する
# 単語の重複表示は無効化する
wc = WordCloud(background_color="white",
               mask=mask,  # マスクを指定
               font_path="/usr/share/fonts/meiryo/meiryo.ttc",
               width=5000, height=3600,
               collocations=False)

wordcloud = wc.generate(" ".join(words))

# ワードクラウドを表示する
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# ワードクラウドをDPI350でファイルに保存する
plt.figure(figsize=(wordcloud.width / 100, wordcloud.height / 100), dpi=350)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig(output_file, format='png', bbox_inches='tight', pad_inches=0)
plt.close()
