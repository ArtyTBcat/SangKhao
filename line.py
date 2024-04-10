import requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

URL = 'https://notify-api.line.me/api/notify'
TOKEN = "pJclaEiUT45a4Ns9jMDlR3DPKyIgg5wZVIzUtGTclvD"
HEADER = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + TOKEN}

def sendline(msg: str = None):
    print("running")
    r = requests.post(URL, headers=HEADER, data={'message': msg})
    print(f"{'': <10}Line message: {r.text}")

app = Flask(__name__)

# Replace with your Channel Access Token and Channel Secret
line_bot_api = LineBotApi('Lp7MNRTJcb/Xs6xr/9zfm5J2Sz3EbW09kVF5HaMcYqhSAWPF8GE3WtAJol443IvAoBjGZGs5wpGKSxsg7xYtJ39fTXMBrQ14iEfebbTuWyMLqDpZ7q3KbcpSflKLGaYsCwNIPKIcGA6WgpuFEzURhwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f994a4599c2640159dd84667df28031b')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("handle_message event triggered")
    print(event.reply_token)
    message_text = event.message.text
    import main
    reply_message = main.API_reply_msg
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

if __name__ == "__main__":
    app.run()




