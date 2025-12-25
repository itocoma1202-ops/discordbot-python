# インストールした discord.py を読み込む
import discord
import os
from dotenv import load_dotenv
from flask import Flask


# ソケットの作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# .envファイルの内容を読み込む
load_dotenv()

#Render用のflaskアプリの設定


#intents関連
intents=discord.Intents.none()
intents.reactions = True
intents.guilds = True

# 環境変数を取得
TOKEN = os.getenv("D_TOKEN")

# 自分のBotのアクセストークンに置き換えてください
#TOKENのから揚げｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱwwwwwwwwwwwwwwwwwwwww
# discord.py Ver2.0 以降は必要
#intent.message_content = True
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    #テストメッセ―ジ
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
