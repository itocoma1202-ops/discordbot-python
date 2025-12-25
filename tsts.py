import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

# 環境変数を取得
innyou = os.getenv("D_TOKEN")


# 結果を表示
print(innyou)

