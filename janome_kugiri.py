from janome.tokenizer import Tokenizer
import codecs
import sys

# Tokenizerのインスタンスを作成
t = Tokenizer()

# 第1引数から入力ファイル名を取得
input_filename = sys.argv[1]

# テキストファイルを開く
with codecs.open(input_filename, 'r', 'utf-8') as f:
    text = f.read()

# テキストを形態素解析
tokens = t.tokenize(text)

# 第2引数から出力ファイル名を取得
output_filename = sys.argv[2]

# 出力用のテキストファイルを開く
with codecs.open(output_filename, 'w', 'utf-8') as f:
    # 各トークン（単語）を出力ファイルに書き込む
    for token in tokens:
        f.write(str(token.surface) + "\n")

