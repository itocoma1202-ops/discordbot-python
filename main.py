# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'MTQ1Mjk4NTk2NDMxMzE4MjIwOA.Gjf62C.FVuHQEzyM1o0sa-OzgNRMRF2mDAaFGx7nnWlyI'

#
# discord.py Ver2.0 以降は必要
#intent.message_content = True
client = discord.Client(intents=discord.Intents.default())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
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
