from flask import Flask, request, abort
 from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
 app = Flask(__name__)
 line_bot_api = LineBotApi('S/uMyi3L9Ghrd9ZXe/u1CPnpd/mg85R7OX3MwR27RztSHN0Er/6O1jic/AvUTLwv8NX+K86AoJmwEE7z0eEGEkEt8d39PItYqgSAC3IPTSeH0Wq5b4qXoTjGE0ep1l4C0wPJIDwBmJQg+R+ak63o6QdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('8ac5c9557affc71faf51bd3ab8234e9a')
 @app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
     # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
     # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
     return 'OK'
 @handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
		profile = line_bot_api.get_progile(user_id)
        event.reply_token,
		texttoreply=('Nice to meet you, '+profile.display_name)
        TextSendMessage(text=texttoreply))
 if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
