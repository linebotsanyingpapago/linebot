from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexBubble,
    FlexImage,
    FlexMessage,
    FlexBox,
    FlexText,
    FlexIcon,
    FlexButton,
    FlexSeparator,
    FlexContainer,
    URIAction,
    Emoji,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    ImageMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import json
import os

app = Flask(__name__)

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        
        if text == '四季探索':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                )
            )

        elif text == '春意旅程':#四季探索
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '盛夏藍藝':#四季探索
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
         
        elif text == '秋韻漫步':#四季探索
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
         
        elif text == '冬日奇遇':#四季探索
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
              
        elif text == '炎夏狂歡':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
              
        elif text == '金秋盛宴':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
              
        elif text == '春日盛典':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
              
        elif text == '雪舞冬日':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
              
        elif text == '綠色足跡':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
               
        elif text == '文化旅程':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '美食推薦':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '饗三峽':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                
        elif text == '饗鶯歌':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                
        elif text == '交通資訊':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '中文lineplay':#中文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == 'explorations':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'SpringVoyage':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'SummerIndigoJourney':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'AutumnStroll':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'WinterSerenityVoyage':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'SpringCelebrations':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == 'SummerCelebrations':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'AutumnCelebrations':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'WinterCelebrations':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
              
        elif text == 'greenfootprint':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == 'culturaljourney':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == 'food':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'FeastSanxia':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == 'FeastYingge':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
           
        elif text == 'news&events':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
          
        elif text == '英文lineplay':#英文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
#============================================================================================================================            
        elif text == '사계절탐색':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '봄의여정':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '여름쪽빛염색여행':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '가을여행':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '겨울고요의여정':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '봄철탐험':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '여름철탐험':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '가을철탐험':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '겨울철탐험':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )

#=====================================================================================================================
                
        elif text == '녹색발자국':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '문화여정':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '맛있는음식':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '향산샤':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '향잉거':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                
        elif text == '교통정보':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '韓文lineplay':#韓文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '探検':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                
        elif text == '春の旅':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '夏の藍染め旅':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '秋の日の散歩':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '冬の静寂な旅':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
          
        elif text == '夏の探索':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '冬の探索':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '秋の探索':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '春の探索':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )   
        elif text == '緑の足跡':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '文化の旅路':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                
        elif text == '美味しい料理':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        
        elif text == '饗三峡日':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
            
        elif text == '饗鶯歌日':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
               
        elif text == '交通情報':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                
        elif text == '日文lineplay':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )   
                
        elif text == 'Test':
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )  
                
        elif text == 'testimage':
            url = request.url_root + 'static/185784.jpg'
            url = url.replace("http", "https")
            app.logger.info("url=" + url)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(original_content_url=url, preview_image_url=url),
                        TextMessage(text="這是文字訊息")
                    ]
                )
            )
        
        elif text == '綠色足跡影片(中)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/Urmos7jUC0o")]
                )
            )
        elif text == '綠色足跡影片(英)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/sZfk58fKO_Q")]
                )
            )
        elif text == '陶藝物語影片(中)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/ZAtdBUkAx3I")]
                )
            )
        elif text == '陶藝物語影片(英)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/2GJN-eUMhF4")]
                )
            )
        elif text == '染出美好影片(中)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/fJ4RndG4NNc")]
                )
            )
        elif text == '染出美好影片(英)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/drDJB5klxL0")]
                )
            )
        elif text == '茶鄉故事影片(英)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/AJr10lmqab8")]
                )
            )
        elif text == '茶鄉故事影片(中)':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="https://youtu.be/BGVY_TYLMzk")]
                )
            )
#***********************************************************************************************************************************
        elif text == '三峽藍染中心簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「傳承藍染，延續工藝的魅力」\n\n三峽藍染中心以體驗教學與藍染商品為主要服務，致力於保存藍染文化。喜歡創意又有趣的手工藝嗎？那就跟我們一起來探索藍染中心吧！\n這裡不僅能學習獨特的藍染藝術，還能親自體驗藍染工藝，打造屬於自己的藍染作品🖼️，體驗手作的樂趣，帶回的不只是作品，還有滿滿的知識與成就感🥳\n\n📌營業資訊\n聯絡電話：02-86713108  \n營業時間：  \n星期一：休息\n星期二－星期日 10:00-17:00\n\n想要瞭解藍染工藝的知識與文化嗎？\n那就跟我們一起來三峽藍染中心吧！")]
                )
            )
        elif text == '三峽藍染中心Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The Sanxia Indigo Dyeing Center offers hands-on experiences and unique indigo-dyed products, dedicated to preserving the rich tradition of indigo dyeing. Are you a fan of creative and fun handicrafts? Then come explore the world of indigo dyeing with us!\nHere, you can not only learn about the fascinating art of indigo dyeing but also experience the process yourself, creating your own indigo-dyed masterpiece 🖼️. Enjoy the joy of crafting, and leave with not only your artwork but also a wealth of knowledge and a sense of accomplishment 🥳.\n\n📌 Business Information\nContact Number: +886-2-86713108\nOperating Hours:\nMonday: Closed\nTuesday - Sunday: 10:00 AM - 5:00 PM\n\nWant to learn more about indigo dyeing techniques and its cultural significance?\n\nThen come visit us at Sanxia Indigo Dyeing Center!")]
                )
            )
        elif text == '三峽藍染中心紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="三峡藍染センターは、藍染文化の保存に力を入れ、体験学習と藍染商品を提供しています。\nクリエイティブで楽しい手工芸が好きですか？それなら、私たちと一緒に藍染センターを探索してみましょう！\nここでは、ユニークな藍染アートを学ぶことができるだけでなく、実際に藍染工芸を体験し、自分だけの藍染作品 🖼️ を作ることができます。手作りの楽しさを感じながら、作品とともに知識と達成感 🥳 を持ち帰りましょう。\n\n📌 営業情報\n電話番号：+886-2-86713108\n営業時間：\n月曜日：休業\n火曜日～日曜日：10:00 AM - 5:00 PM\n\n藍染技術とその文化的な意味についてもっと知りたいですか？\n\nそれなら、ぜひ三峡藍染センターにお越しください！\n")]
                )
            )
        elif text == '三峽藍染中心소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="삼협 블루 다이 센터는 체험 학습과 블루 다이 제품을 주 서비스로 제공하며, 블루 다이 문화를 보존하는 데 힘쓰고 있습니다. 창의적이고 재미있는 수공예를 좋아하나요? 그렇다면 저희와 함께 블루 다이 센터를 탐험해 보세요!\n여기에서는 독특한 블루 다이 예술을 배우는 것뿐만 아니라, 직접 블루 다이 공예를 체험하고 나만의 블루 다이 작품 🖼️ 을 만들 수 있습니다. 손으로 만드는 즐거움을 느끼며, 작품뿐만 아니라 지식과 성취감 🥳 을 함께 가져가세요.\n\n📌 영업 정보\n전화 번호: +886-2-86713108\n운영 시간:\n월요일: 휴무\n화요일 – 일요일: 10:00 AM - 5:00 PM\n\n블루 다이 기술과 그 문화적 의미에 대해 더 알고 싶으신가요?\n\n그렇다면 삼협 블루 다이 센터로 오세요!")]
                )
            )
        elif text == '三峽老街簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「漫步百年紅磚🧱，感受三峽老街的古韻新風~」\n\n三峽老街是台灣保存最完整、最具歷史意義的傳統街道之一，擁有百年歷史的紅磚拱廊與精美的巴洛克建築風格，展現出濃厚的懷舊氛圍🏮。不可錯過的是 三峽祖師廟🏯，這座精雕細琢的廟宇是藝術與信仰的結晶。此外，老街上的藍染工藝更是三峽的文化亮點，遊客可體驗DIY藍染，將這份傳統技藝帶回家。無論是漫步於紅磚長廊、品嚐在地特色小吃，還是欣賞文化工藝，三峽老街都以其獨特的魅力吸引著異國旅客🌍，帶您穿越時光，體驗台灣的古早風情。\n\n📌營業資訊\n聯絡電話:\n02-26789571\n營業時間：全年無休\n快來三峽老街，帶你走入古色古香的時光大道~")]
                )
            )    
        elif text == '三峽老街Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Sanxia Old Street is one of Taiwan's best-preserved and most historically significant traditional streets, featuring century-old red brick arcades and exquisite Baroque architecture that evoke a nostalgic atmosphere 🏮. A must-see is the Sanxia Zushi Temple 🏯, a finely crafted temple that blends art and faith. Additionally, the indigo dyeing craft on the street is another cultural highlight of Sanxia, where visitors can experience DIY indigo dyeing and take home this traditional skill. Whether you're strolling through the red brick arcades, tasting local delicacies, or admiring cultural crafts, Sanxia Old Street attracts international travelers 🌍 with its unique charm, offering a journey through time and a taste of Taiwan's old-world flavor.\n\n📌Operating Information\nPhone: +886-2-26789571\nOpening Hours:  Open year-round\nCome to Sanxia Old Street and step into the timeless charm of history~")]
                )
            )
        elif text == '三峽老街紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="三峡老街は台湾で最も保存状態が良く、歴史的にも重要な伝統的な街道の一つです。100年以上の歴史を持つ赤レンガのアーケードと美しいバロック様式の建築は、懐かしい雰囲気を醸し出しています🏮。見逃せないのは三峡祖師廟🏯で、この精緻に彫刻された寺院は、芸術と信仰の結晶です。また、老街に並ぶ藍染工芸は三峡の文化のハイライトであり、訪れる人々はDIY藍染体験をして、伝統的な技術を自宅に持ち帰ることができます。赤レンガのアーケードを歩いたり、地元の特産品を味わったり、文化的な工芸品を鑑賞したりと、三峡老街はその独特な魅力で世界中の観光客を惹きつけています🌍。台湾の古き時代の風情を体験するために、三峡老街にお越しください。\n\n📌 営業情報\n電話番号：+886-2-26789571\n営業時間：年中無休\n三峡老街にぜひ足を運び、時を超えた歴史の道を歩んでください~")]
                )
            )
        elif text == '三峽老街소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="삼협 올드 스트리트는 대만에서 가장 잘 보존된 역사적인 거리 중 하나로, 100년 이상의 역사를 자랑하는 붉은 벽돌 아케이드와 정교한 바로크 건축 양식이 어우러져 깊은 향수를 자아냅니다🏮. 놓칠 수 없는 명소는 삼협 조사묘🏯로, 이 정교하게 조각된 사원은 예술과 신앙의 결합체입니다. 또한, 거리 곳곳에 있는 인디고 염색 공예는 삼협의 문화적 하이라이트로, 방문객들은 DIY 인디고 염색 체험을 통해 전통 기법을 집으로 가져갈 수 있습니다. 붉은 벽돌 아케이드를 거닐거나, 지역 특산 음식을 맛보거나, 문화 공예를 감상하는 등 삼협 올드 스트리트는 그 독특한 매력으로 전 세계의 여행객들을 끌어들입니다🌍. 대만의 옛 정취를 경험하고 싶다면 삼협 올드 스트리트로 오세요.\n\n📌 영업 정보\n전화: +886-2-26789571\n영업시간: 연중무휴\n삼협 올드 스트리트로 오셔서, 시간을 초월한 역사적인 길을 걸어보세요~")]
                )
            )
        elif text == '鶯歌老街簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「陶韻悠揚，漫遊鶯歌老街~」\n\n鶯歌老街是一條充滿歷史與文化氣息的傳統街道，素有「陶瓷之鄉」的美譽。這裡不僅保留了台灣最具特色的陶瓷藝術，還融合了傳統古街的魅力，是探索台灣手工藝和歷史文化的好地方。從傳統的陶碗🥣、陶壺🫖，到現代創新的陶藝作品，都能在這裡找到。街道上還有許多歷史悠久的建築，與古老的巷弄交織出一幅幅別具韻味的風景畫🖼️。\n\n📌營業資訊\n聯絡電話：02-26780202\n營業時間： 全年無休\n快來鶯歌老街，跟我們一起沉醉在充滿文藝氣息的陶瓷老街🤩")]
                )
            )
        elif text == '鶯歌老街Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Yingge Old Street is a traditional street filled with history and cultural charm, renowned as the 'Town of Ceramics.'' Here, you can not only experience Taiwan's most distinctive ceramic art but also immerse yourself in the charm of traditional old streets. It's the perfect place to explore Taiwan’s handcrafts and cultural heritage. From traditional ceramic bowls 🥣 and teapots 🫖 to modern and innovative ceramic art pieces, you’ll find it all here. The street is lined with historical buildings, blending with ancient alleyways to create a picturesque scene 🖼️.\n\n📌 Business Information\nContact Number:+886-2-26780202\nOpening Hours: Open Year-Round\nCome to Yingge Old Street, and let’s get lost in this art-filled ceramic haven 🤩")]
                )
            )
        elif text == '鶯歌老街紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌老街は、歴史と文化が息づく伝統的な通りで、「陶磁器の里」として有名です。ここでは、台湾で最も特徴的な陶磁器アートを堪能できるだけでなく、伝統的な古街の魅力も感じることができます。台湾の手工芸と歴史文化を探るのにぴったりの場所です。伝統的な陶器の碗🥣や茶壺🫖から、現代的で革新的な陶芸作品まで、ここで全て見つけることができます。街並みには歴史的な建物が並び、古い路地と交差して、一つ一つが趣のある風景画🖼️を作り出しています。\n\n📌 営業情報\n電話番号：+886-2-26780202\n営業時間：年中無休\nぜひ鶯歌老街に足を運び、陶芸のアートと歴史が息づくこの場所に浸ってください🤩")]
                )
            )
        elif text == '鶯歌老街소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="영거 올드 스트리트는 역사와 문화가 가득한 전통적인 거리로, '도자기 마을'로 잘 알려져 있습니다. 여기에서는 대만에서 가장 독특한 도자기 예술을 경험할 수 있을 뿐만 아니라, 전통적인 옛 거리의 매력을 만끽할 수 있습니다. 대만의 수공예와 역사적 문화를 탐험하기에 최적의 장소입니다. 전통적인 도자기 그릇🥣과 찻주전자🫖부터 현대적이고 혁신적인 도자기 작품까지, 이곳에서는 모두 찾아볼 수 있습니다. 거리는 역사적인 건물로 가득하며, 오래된 골목과 어우러져 그림 같은 풍경을 만들어냅니다 🖼️.\n\n📌 영업 정보\n전화번호: +886-2-26780202\n운영 시간: 연중 무휴\n영거 올드 스트리트로 오셔서, 예술적 분위기가 가득한 도자기 거리에서 한껏 빠져보세요 🤩")]
                )
            )
        elif text == '天芳茶行簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「一心二✌🏻，三角湧」\n\n天芳茶行是經營百年傳承五代的老茶行，擁有自己的茶園與製茶廠，近幾年，透過農會的輔導更開始結合觀光與導覽，推出手作製茶的體驗課程，藉此讓民眾深入瞭解茶產業的文化❗️秉持傳承百年的製茶工藝精神，為老茶行注入新思維，藉此豎立年輕化的品牌形象，以誠心、踏實的態度，製作出高品質的茶葉🥰\n\n📌營業資訊\n參觀時間: 周一〜週日08:30-22:00 \n採茶體驗:採預約制10人開課 \n預約電話:02-26726808 \n行動電話:0929-330-209 \n如果你想更加瞭解茶葉製成\n那就跟我們一起來天芳茶行看看吧！")]
                )
            )
        elif text == '天芳茶行Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Tianfang Tea House is a historic tea shop that has been passed down through five generations, with its own tea plantations and tea production facilities. In recent years, with guidance from the agricultural association, they have started to incorporate tourism and guided tours. They offer hands-on tea-making experiences, allowing visitors to deeply explore the culture of the tea industry. By preserving the spirit of traditional tea-making craftsmanship, they have injected new ideas into the old tea business, establishing a youthful brand image. With sincerity and dedication, they continue to produce high-quality tea leaves. 🥰\n\n📌 Business Information\nVisiting Hours: Monday–Sunday, 08:30–22:00\nTea-picking Experience: By appointment, 10 people per session\nReservation Phone:+886-22672-6808\nMobile Phone: +886-929-330-209\nIf you want to learn more about the process of tea production, come visit Tianfang Tea House with us!")]
                )
            )
        elif text == '天芳茶行紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="天芳茶行は、五代にわたり百年の伝統を誇る老舗の茶屋で、自社の茶畑と製茶工場を持っています。近年では農協の支援を受け、観光とガイドツアーを取り入れ、手作りの製茶体験を提供するようになり、来訪者に茶産業の文化を深く知ってもらうことができます❗️伝統的な製茶技術の精神を大切にし、古くからの茶屋に新しい視点を注ぎ込むことで、若者向けのブランドイメージを確立しています。誠実で堅実な姿勢で、高品質な茶葉を作り続けています🥰\n\n📌 営業情報\n見学時間: 月曜日〜日曜日、08:30〜22:00\n茶摘み体験: 予約制、10名から開催\n予約電話: +886-22672-6808\n携帯電話:  +886-929-330-209\nお茶の製造過程についてもっと知りたいなら、天芳茶行に一緒に行ってみましょう！")]
                )
            )
        elif text == '天芳茶行소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="천방차행은 5대에 걸쳐 전해 내려온 100년 전통의 오래된 찻집으로, 자체 차밭과 차 제조 공장을 운영하고 있습니다. 최근 몇 년 동안 농협의 지원을 받아 관광과 가이드 투어를 결합하고, 손으로 차를 만드는 체험 프로그램을 제공하여, 방문객들이 차 산업 문화에 대해 깊이 이해할 수 있도록 하고 있습니다❗️ 전통적인 차 제조 기술 정신을 고수하면서, 오래된 찻집에 새로운 아이디어를 주입하여, 젊은 브랜드 이미지를 세우고 있습니다. 성실하고 철저한 태도로 고품질 차잎을 생산하고 있습니다🥰\n\n📌 영업 정보\n관람 시간: 월요일~일요일 08:30-22:00\n차 따기 체험: 예약제로 10명부터 진행\n예약 전화: +886-22672-6808\n휴대전화:  +886-929-330-209\n차 제조 과정에 대해 더 알고 싶다면, 천방차행에 함께 가보세요!")]
                )
            )
        elif text == '茶業歷史文物館簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「品味歷史，尋找茶的故事🍵」\n\n大板根茶業歷史文物館傳承歷史文化財產，見證百年文化歷史軌跡。\n大板根曾經是臺灣最重要的茶業生產重鎮，資料記載要追朔到日治時代，日本的三井合名會社引進現代化的製作紅茶技術，地點就在三峽大豹溪旁來設立三井大寶製茶工廠，這裡也是當年東亞地區最大的製茶廠🏭，也是當時是日本三井合名會社八座製茶工廠中規模最大的製茶廠，當時他們所生產的茶葉是名聞遐邇的「日東紅茶」☕️\n\n📌營業資訊\n聯絡電話：02-26749228\n營業時間：全年開放\n想要瞭解茶業歷史文化？\n那就來大板根茶業歷史文物館吧！🏛️")]
                )
            )
        elif text == '茶業歷史文物館Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="DabanGen Tea Industry History Museum preserves historical and cultural heritage, witnessing over a century of tea culture history.\nDabanGen was once one of Taiwan's most important tea production hubs. Historical records trace back to the Japanese colonial era when the Mitsui Company introduced modern black tea production techniques and established the Mitsui Dabo Tea Factory by the Dabaoxi River in Sanxia. This factory was the largest in East Asia at the time and also the largest among the eight tea factories owned by the Mitsui Company in Japan. The tea produced here was renowned far and wide as 'Nitto Black Tea' ☕️.\n\n📌 Business Information\nContact Number: +886-2-26749228\nOperating Hours: Open Year-Round\nInterested in learning about the history and culture of tea?\nThen come visit the DabanGen Tea Industry History Museum! 🏛️")]
                )
            )
        elif text == '茶業歷史文物館紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="大板根茶業歴史文物館は、歴史的な文化遺産を保存し、百年にわたる茶業文化の軌跡を見守っています。\n大板根はかつて台湾で最も重要な茶業生産の中心地であり、その歴史は日本統治時代に遡ります。三井合名会社が現代的な紅茶製造技術を導入し、三峡大豹渓の近くに三井大宝製茶工場を設立しました。この工場は、当時、東アジアで最大規模の製茶工場であり、日本三井合名会社が運営する8つの製茶工場の中でも最も大きな工場でした。ここで生産された茶葉は、広く「日東紅茶」として知られていました☕️。\n\n📌 営業情報\n電話番号：+886-2-26749228\n営業時間：年中無休\n茶業の歴史と文化について知りたいですか？\nそれなら、大板根茶業歴史文物館にぜひお越しください！ 🏛️")]
                )
            )
        elif text == '茶業歷史文物館소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="대반근 차업 역사 문물관은 역사적 문화유산을 계승하며, 백년 동안의 차 산업 문화의 흔적을 목격해 왔습니다.\n대반근은 한때 대만에서 가장 중요한 차 생산 중심지였으며, 그 역사는 일본 통치 시대까지 거슬러 올라갑니다. 미쓰이 합명회사가 현대적인 홍차 제조 기술을 도입하고, 삼협 대호계 근처에 미쓰이 대보 차 공장을 설립했습니다. 이 공장은 당시 동아시아에서 가장 큰 차 공장이었으며, 일본 미쓰이 합명회사가 운영하는 8개 차 공장 중 가장 큰 규모의 공장이었습니다. 여기에서 생산된 차는 '닛토 홍차'로 널리 알려졌습니다 ☕️.\n\n📌 영업 정보\n전화 번호: +886-2-26749228\n운영 시간: 연중 무휴\n차 산업의 역사와 문화를 알고 싶다면?\n그렇다면 대반근 차업 역사 문물관에 꼭 방문해 보세요! 🏛️")]
                )
            )
        elif text == '清水祖師廟簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「傳說中的東方藝術殿堂」🏛️\n\n建於西元1767年的三峽祖師廟，又稱三峽長福巖，供奉來自福建泉州安溪縣的高僧清水祖師。在寺廟250年歷史中，曾經歷3次修建，最後一次自1947年開始，由在地的藝術家李梅樹主導。李梅樹對祖師廟的建築與設計極其用心，寺廟因而名譟一時，不僅成為三峽的代名詞，更博得「東方藝術殿堂」的美名。其特色以木🪵為頂、以石🪨為基的建築，採五門三殿式的格局，廟頂層層疊疊，每根脊上都有富麗堂皇的裝飾，廟內則無處不雕、無處不琢。\n\n📌營業資訊\n聯絡電話：02-26711031\n營業時間：全年開放\n想要來訪傳說中的東方藝術殿堂嗎？\n那就來三峽清水祖師廟看看吧！")]
                )
            )
        elif text == '清水祖師廟Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Built in 1767, the Sanxia Qingshui Zushi Temple, also known as Sanxia Changfu Rock, is dedicated to Qingshui Zushi, a renowned monk from Anxi County, Quanzhou, Fujian. Over its 250-year history, the temple has undergone three reconstructions, with the most recent one starting in 1947, led by local artist Li Meishu. Li’s meticulous attention to the temple’s architecture and design made it famous, earning the temple the title of the 'Eastern Art Hall.'\nThe temple is known for its unique architectural style, with wooden roofs 🪵 and a stone foundation 🪨, following a five-entrance, three-hall layout. The multi-tiered roof is adorned with magnificent decorations on every ridge, and the interior is intricately carved, with no corner left undecorated.\n\n📌 Business Information\nContact Number: +886-2-26711031\nOperating Hours: Open Year-Round\nWant to visit the legendary Eastern Art Hall?\nCome see the Sanxia Qingshui Zushi Temple!")]
                )
            )
        elif text == '清水祖師廟紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「伝説の東方芸術殿堂」 🏛️\n\n1767年に建てられた三峡清水祖師廟（三峡長福巖）は、福建省泉州市安渓県出身の高僧清水祖師を祀っています。250年の歴史の中で、寺院は3回の修復を経て、最も最近の修復は1947年に地元の芸術家である李梅樹の指導の下で行われました。李梅樹の細心の注意を払った建築とデザインにより、この寺院は一躍有名となり、「東方芸術殿堂」として名を馳せました。\nこの寺院は、木製の屋根 🪵と石造の基礎 🪨を特徴とする、五門三殿の構造を採用しています。屋根は多層構造で、すべての脊には豪華な装飾が施され、内部は精緻な彫刻で飾られ、どこもかしこも彫り込まれています。\n\n📌 営業情報\n電話番号： +886-2-26711031\n営業時間：年中無休\n伝説の「東方芸術殿堂」を訪れたくはありませんか？\nぜひ、三峡清水祖師廟にお越しください！")]
                )
            )
        elif text == '清水祖師廟소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="1767년에 건립된 삼협 청수 조사 사원(또는 삼협 장복암)은 푸젠성 취안저우 안계현 출신의 고승 청수 조사를 모시는 사원입니다. 250년의 역사 속에서 이 사원은 3차례의 재건을 거쳤으며, 가장 최근의 재건은 1947년에 지역 예술가 이매수의 주도로 진행되었습니다. 이매수는 사원의 건축과 디자인에 세심한 노력을 기울였으며, 이로 인해 사원은 큰 명성을 얻었고, '동양 예술의 전당'이라는 찬사를 받았습니다.\n사원의 특징적인 건축 양식은 나무로 된 지붕 🪵과 돌로 된 기초 🪨로 이루어져 있으며, 오문 삼전식 구조를 채택하고 있습니다. 지붕은 여러 층으로 쌓여 있으며, 각 기와에는 화려한 장식이 있어 아름다움을 더합니다. 내부는 세밀한 조각과 조각으로 가득 차 있습니다.\n\n📌 영업 정보\n전화 번호: +886-2-26711031\n운영 시간: 연중 무휴\n전설적인 동양 예술의 전당을 방문하고 싶으신가요?\n그렇다면 삼협 청수 조사 사원에 꼭 오세요!")]
                )
            )
        elif text == '李梅樹紀念館簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「雕琢東方藝術殿堂的偉大藝術家」\n\n李梅樹紀念館🕌是一間以紀念臺灣畫家李梅樹和展出其作品為宗旨所設立的紀念館，紀念館收藏有李梅樹先生一生傑作及各項文物資料。李教授創作內容以呈現臺灣鄉土之美為主要訴求，畫風走寫實路線，一生最鍾愛的三峽風光畫作🏞️，充滿了他強調的「風、土、民、情」藝術理念。然而他有些作品風格卻極為特殊，例如《戲弄火雞的男孩》採用3D畫法😎，與世界名畫《蒙娜麗莎的微笑》有異曲同工之妙。\n\n📌營業資訊\n聯絡電話：02-26732333\n營業時間：星期六-星期日 10:00-17:00\n想要更瞭解東方藝術殿堂之父的生平事蹟、作品嗎?那就跟我們一起到李梅樹紀念館看看吧！")]
                )
            )
        elif text == '李梅樹紀念館Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The Li Meishu Memorial Hall 🕌 is dedicated to commemorating the Taiwanese painter Li Meishu and showcasing his works. The museum houses a collection of his masterpieces and various cultural artifacts. Prof. Li’s creative focus was on portraying the beauty of Taiwan’s rural landscapes, with his style rooted in realism. His most beloved works feature the scenery of Sanxia 🏞️, embodying his artistic philosophy of 'wind, earth, people, and emotion. However,' some of his works exhibit a highly unique style, such as 'The Boy Teasing the Turkey', which uses a 3D painting technique 😎, reminiscent of the world-renowned 'Mona Lisa's Smile'.\n\n📌 Business Information\nContact Number: +886-2-26732333\nOperating Hours: Saturday - Sunday 10:00 AM - 5:00 PM\nWould you like to learn more about the life and works of the Father of Eastern Art Hall?\nCome visit the Li Meishu Memorial Hall with us!")]
                )
            )
        elif text == '李梅樹紀念館紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="李梅樹記念館 🕌は、台湾の画家李梅樹を記念し、彼の作品を展示することを目的として設立された記念館です。記念館には、李梅樹氏の生涯の傑作やさまざまな文化資料が収められています。李教授の創作内容は、台湾の田舎の美を表現することに焦点を当て、画風は写実主義に基づいています。彼が最も愛した三峡の風景画🏞️は、彼が強調した「風・土・民・情」という芸術理念を具現化しています。しかし、彼の作品には非常にユニークなスタイルもあり、例えば**「火鶏をからかう少年」は3D絵画技法を採用しており😎、世界的に有名な「モナ・リザの微笑み」**に似た魅力があります。\n\n📌 営業情報\n電話番号：+886-2-26732333\n営業時間：土曜日 - 日曜日 10:00 AM - 5:00 PM\n東方芸術殿堂の父の生涯と作品についてもっと知りたくはありませんか？\nぜひ、李梅樹記念館にお越しください！")]
                )
            )
        elif text == '李梅樹紀念館소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="이매수 기념관 🕌은 대만 화가 이매수를 기리고 그의 작품을 전시하는 것을 목적으로 설립된 기념관입니다. 기념관에는 이매수 선생님의 생애 작품과 다양한 문화 유물이 소장되어 있습니다. 이 교수의 창작 내용은 대만의 시골 풍경을 아름답게 표현하는 데 초점을 맞추었으며, 그의 화풍은 사실주의에 뿌리를 두고 있습니다. 그가 가장 사랑한 삼협의 풍경화 🏞️는 그가 강조한 「바람, 땅, 사람, 정」 예술 철학을 잘 보여줍니다. 그러나 그의 작품 중 일부는 매우 독특한 스타일을 보이는데, 예를 들어 **「칠면조를 괴롭히는 소년」**은 3D 화법을 사용하여 😎, 세계적인 명화 **「모나리자의 미소」**와 비슷한 매력을 지니고 있습니다.\n\n📌 영업 정보\n전화 번호: +886-2-26732333\n운영 시간: 토요일 - 일요일 10:00 AM - 5:00 PM\n동양 예술의 전당의 아버지의 생애와 작품을 더 알고 싶으신가요?\n그렇다면 이매수 기념관에 꼭 방문해 보세요!")]
                )
            )
        elif text == '鳶山簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「踏上鳶山⛰️，探索大自然的壯麗！」\n\n鳶山登山步道為三峽著名的親山步道，可俯瞰大台北地區的晨昏之美🌄。山頭因形似一隻飛翔的猛禽而得名，鳶山與位於大漢溪北岸的鶯歌石遙遙相望，行駛於國道三號時，兩座山頭一左一右如同進出新北的門柱，是三峽居民休憩運動的後花園，假日更吸引許多遊客前往，黃昏時分來到鳶山，居高臨下眺望大漢溪沖積平原，欣賞三峽、鶯歌、八德地區的萬家燈火🌃，入夜後國道三號的燈火宛如地上的星光般閃爍著🌌，景緻十分耐看，晴朗的夜晚甚至能見到數十公里外臺北市區的天際線，越夜越美麗。\n\n📌營業資訊\n聯絡電話：02-26711017\n營業時間：全年開放\n想要來一場與大自然親密接觸的旅程嗎？\n那就來鳶山跟我們一起探索大自然的光彩吧！")]
                )
            )
        elif text == '鳶山Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Yuan Mountain Trail is one of the most famous mountain trails in Sanxia, offering a breathtaking view of the Greater Taipei area at dawn and dusk 🌄. The mountain is named after its shape, which resembles a soaring bird of prey. Yuan Mountain and the Yingge Stone, located on the north bank of the Dahan River, stand as twin sentinels, one to the left and one to the right, as if marking the entrance and exit of New Taipei. This area serves as a backyard for the residents of Sanxia, where they come to relax and exercise, and it attracts many tourists during weekends. At dusk, ascend Yuan Mountain for a panoramic view of the Dahan River alluvial plain, and marvel at the thousands of lights twinkling across the Sanxia, Yingge, and Bade districts 🌃. As night falls, the lights on National Freeway 3 sparkle like stars on the ground 🌌, creating a mesmerizing sight. On clear nights, you can even catch a glimpse of the Taipei city skyline, dozens of kilometers away, growing more beautiful as the night deepens.\n\n📌 Business Information\nContact Number: +886-2-26711017\nOperating Hours: Open year-round\nReady for a journey to connect with nature?\nCome explore the brilliance of the great outdoors with us at Yuan Mountain!")]
                )
            )
        elif text == '鳶山紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鳶山登山道は三峡の有名な登山道の一つで、大台北地区の美しい朝夕の景色を楽しむことができます🌄。山の形が飛翔する猛禽類に似ていることから、その名が付けられました。鳶山と、大漢渓北岸に位置する鶯歌石は、遠くに向かい合っており、国道3号線を走ると、両山が左右に広がり、新北市への出入り口のように見えます。このエリアは三峡の住民にとっての憩いの場所で、休日には多くの観光客が訪れます。夕方には鳶山に登り、大漢渓の沖積平野を見下ろし、三峡、鶯歌、八德地区の無数の灯り🌃を楽しむことができます。夜になると、国道3号線の灯りは地上の星のようにきらめきます🌌。晴れた夜には、台北市区のシルエットも数十キロ先に見ることができ、夜が深くなるにつれてその美しさは増していきます。\n\n📌 営業情報\n電話番号：+886-2-26711017\n営業時間：年中無休\n自然との親密な接触を感じる旅に出かけませんか？\n鳶山で私たちと一緒に、自然の輝きを探しに行きましょう！")]
                )
            )
        elif text == '鳶山소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="연산 등산로는 삼협에서 유명한 등산로로, 대만 북부 지역의 아름다운 아침과 저녁 풍경을 감상할 수 있는 명소입니다🌄. 연산은 그 모습이 날아오르는 맹금류와 비슷하여 이름이 붙여졌습니다. 연산과 대한강 북쪽에 위치한 영가석은 멀리서 마주 보며, 국도 3호선을 달리면 두 산이 좌우로 자리잡고 있어 마치 신베이시로 들어가는 입구와 출구처럼 보입니다. 이 지역은 삼협 주민들이 쉬고 운동하는 장소로, 주말이면 많은 관광객들이 방문합니다. 황혼이 지면 연산에 올라 대한강 충적 평야를 내려다보며 삼협, 영가, 바더 지역의 수많은 불빛🌃을 즐길 수 있습니다. 밤이 되면 국도 3호선의 불빛이 마치 지상의 별처럼 반짝이며🌌, 맑은 날 밤에는 수십 킬로미터 떨어진 타이페이 시내의 스카이라인도 보일 수 있으며, 밤이 깊어질수록 더욱 아름다운 풍경을 감상할 수 있습니다.\n\n📌 영업 정보\n전화 번호: +886-2-26711017\n운영 시간: 연중 무휴\n자연과의 친밀한 만남을 원하시나요?\n연산에서 자연의 빛나는 아름다움을 함께 탐험해 보세요!")]
                )
            )
        elif text == '滿月圓國家森林遊樂區簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「走進滿月圓，感受大自然的美麗與寧靜！」\n滿月圓森林遊樂區位於三峽大豹溪上游，為中低海拔天然闊葉林森林形態🌲。春夏時分，滿園蝴蝶飛舞🦋，秋冬時分，楓情萬種🍁，一年四季的自然景觀不盡相同。園區內的設施與自然結合，減少人為的破壞，無障礙空間設置完整，適合各年齡層造訪，主步道可觀瀑布、森林浴、賞蝶、賞楓，是北台灣非常受歡迎的森林遊樂區，全新遊客中心在2019年整建完成，增設互動AR設施，非常適合親子共遊🐾！\n\n📌營業資訊\n聯絡電話：02-26720004\n營業時間：全年開放\n\n想要來一場與大自然共舞的旅程嗎?\n\n那就來滿月圓國家森林遊樂區吧！")]
                )
            )
        elif text == '滿月圓國家森林遊樂區Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Full Moon Round National Forest Recreation Area is located in the upper reaches of Daba Creek in Sanxia. It is a mid-low altitude broadleaf forest area 🌲. In spring and summer, butterflies dance freely 🦋, and in autumn and winter, the maples are full of vibrant colors 🍁. The park integrates facilities with nature to minimize human impact, with barrier-free spaces designed to be accessible for all ages. The main trails offer views of waterfalls, opportunities for forest bathing, butterfly watching, and maple leaf viewing. The park is one of the most popular forest recreation areas in northern Taiwan. In 2019, a newly renovated visitor center was opened, featuring interactive AR facilities, making it ideal for family visits 🐾!\n\n📌 Operating Hours:\nContact: +886-2-26720004\nHours: Open year-round\n\nWant to experience the beauty of nature?\n\nVisit Full Moon Round National Forest Recreation Area now!")]
                )
            )       
        elif text == '滿月圓國家森林遊樂區紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="満月園国家森林遊楽区 は三峡の大豹溪上流に位置し、中低海抜の天然広葉樹林の森林地帯です🌲。春と夏には蝶々が舞い、秋と冬にはカエデの美しい紅葉が楽しめます🍁。公園内の施設は自然と調和し、人間の影響を最小限に抑えています。また、バリアフリー設計が整備されており、全ての年齢層の訪問者に適しています。メインのトレイルでは滝、森林浴、蝶々観察、紅葉狩りが楽しめ、北台湾で非常に人気のある森林遊楽区です。2019年にリニューアルされた新しいビジターセンターには、インタラクティブなAR設備も追加されており、親子で楽しむのに最適です🐾！\n\n📌 営業時間：\n連絡先: +886-2-26720004\n営業日: 年中無休\n\n大自然との触れ合いを体験したいですか？\n\n満月園国家森林遊楽区 へ行ってみましょう！")]
                )
            )
        elif text == '滿月圓國家森林遊樂區소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="만월원 국가 숲속 놀이공원 은 삼峡 대포천 상류에 위치한 중저해발 자연 활엽수 숲입니다🌲. 봄과 여름에는 나비들이 춤을 추고🦋, 가을과 겨울에는 단풍이 화려하게 물듭니다🍁. 공원 내 시설은 자연과 잘 결합되어 인간의 영향을 최소화하며, 모든 연령대의 방문객이 쉽게 이용할 수 있도록 배리어 프리 공간이 마련되어 있습니다. 주요 산책로에서는 폭포, 숲속욕, 나비 관찰, 단풍 관람 등을 즐길 수 있습니다. 북부 대만에서 매우 인기 있는 숲속 놀이공원이며, 2019년에 새롭게 리모델링된 방문자 센터에는 인터랙티브 AR 시설이 추가되어 있어 가족 단위 방문객에게 적합합니다🐾!\n\n📌 운영 시간:\n연락처: +886-2-26720004\n운영 시간: 연중무휴\n\n자연과 함께하는 여행을 떠나고 싶나요?\n\n만월원 국가 숲속 놀이공원 에 방문해 보세요!")]
                )
            )
        
        elif text == '新北市客家文化園區簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「走進客家文化園區，品味傳統與創新的交織！」 🏯🎶\n\n新北市客家文化園區環狀的土樓外觀十分吸睛，讓遊客可以透過這些客家生活文物⛱️、作品及傳統民俗玩具🪅，進一步認識客家文化。除提供與客家文化相關展覽外，還有小朋友最喜歡的故事屋，假日不時會舉辦各種客家DIY體驗活動，客家電視館裡也提供現場主播播報體驗及精彩影集播放等，園區內的活動類型豐富多元，適合闔家大小玩上一天🤩。\n\n📌營業資訊\n聯絡電話：02-26729996\n營業時間：  \n星期一-星期五 9：00∼17：00\n星期六-星期日 9：00∼ 18：00\n休館時間：每個月第一個星期一\n\n如果你想更加了解台灣傳統的客家文化\n\n那就跟我們一起來新北市客家文化園區吧！")]
                )
            )
        elif text == '新北市客家文化園區Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The circular architecture of the Hakka-style earth buildings at New Taipei City Hakka Culture Park is quite eye-catching. Visitors can learn more about Hakka culture through the exhibits of Hakka lifestyle artifacts, artworks, and traditional toys. In addition to exhibitions related to Hakka culture, the park features a storytelling house for children, making it a great destination for families. On weekends, there are various DIY activities that allow visitors to experience traditional Hakka crafts. The Hakka TV station also offers a live broadcast experience and exciting TV shows, providing a fun and educational experience for all ages.🤩\n\n📌Operating Information\nContact Phone: +886-2-26729996\nHours of Operation:\nMonday to Friday: 09:00∼17:00\nSaturday to Sunday: 09:00∼18:00\nClosed: The first Monday of every month\n\nIf you want to learn more about Taiwan's traditional Hakka culture, join us at the New Taipei City Hakka Cultural Park!")]
                )
            )
        elif text == '新北市客家文化園區紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="新北市客家文化園區は、客家文化を探求するための最適な場所で、円形の客家スタイルの土楼の外観が多くの訪問者を惹きつけています。園内には、客家の生活文物や工芸品、民俗玩具などの展示があり、客家の歴史と文化を深く理解することができます。さらに、子供向けのストーリーハウスやDIY体験などもあり、家族みんなで楽しめるアクティビティが充実しています。また、客家テレビ館では、現場でのアナウンサー体験や面白いテレビ番組が放送され、客家文化をより深く体験できます🤩。\n\n📌 営業情報\n連絡先：+886-2-26729996\n営業時間：\n月曜日～金曜日：09:00∼17:00\n土曜日～日曜日：09:00∼18:00\n休館日：毎月第1月曜日\n\n台湾の伝統的な客家文化についてもっと知りたいなら、新北市客家文化園区へぜひお越しください！")]
                )
            )
        elif text == '新北市客家文化園區소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="신북시 객가문화공원은 그 독특한 원형 객가식 토루 건축물로 눈길을 끌며, 방문객들이 객가 문화에 대해 더 잘 이해할 수 있도록 돕습니다. 공원은 객가 생활 유물, 작품, 전통 민속 장난감 등을 전시하여 객가 문화의 깊이를 느낄 수 있는 기회를 제공합니다. 이 외에도 어린이들이 좋아하는 이야기 집이 있으며, 주말에는 다양한 객가 DIY 체험 활동도 진행됩니다. 객가 텔레비전관에서는 현장 아나운서 체험 및 흥미로운 TV 프로그램이 방송되어 방문객들이 객가 문화에 대해 더 가까이 느낄 수 있습니다. 다양한 활동이 마련되어 있어 가족 단위 방문객에게 적합한 장소입니다.🤩\n\n📌 운영 정보\n연락 전화:+886-2-26729996\n운영 시간:\n월요일~금요일: 09:00∼17:00\n토요일~일요일: 09:00∼18:00\n휴관일: 매월 첫 번째 월요일\n\n대만의 전통적인 객가 문화를 더 깊이 알고 싶다면, 신베이시 객가 문화 공원으로 함께 가요!")]
                )
            )
        elif text == '庶民美術館簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「藝術走進生活，時間與空間的碰撞」\n\n庶民美術館隱藏在三峽老街上，創立人是老街第三代的年輕藝術家吳冠德，其擅長利用自然取材的樹枝為畫筆🖌️，創作出一幅幅細緻到令人驚豔的油畫作品🎨；其創作也作為「庶民美術館」當中的一大亮點；庶民美術館創立的初衷旨在讓美學走進大眾的日常生活，讓更多人接受藝術的薰陶，因此門票非常親民僅 $30，是三峽老街上不容錯過的私房景點也為三峽老街增添了藝文氣息🫧！\n\n📌營業資訊\n聯絡電話：02-26712009\n營業時間：  \n星期一－星期三：休息\n星期四－星期日：12:00-18:00\n\n想要走進寧靜的百年老屋感受藝術薰陶的光陰？\n\n那就一起來庶民美術館吧！")]
                )
            )
        elif text == '庶民美術館Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Commoner's Art Museum hidden within Sanxia Old Street, the Commoner's Art Museum was founded by Wu Guan-de, a young artist and third-generation resident of the Old Street. Wu is skilled in using naturally sourced tree branches as paintbrushes 🖌️, creating breathtakingly detailed oil paintings 🎨. His works are a highlight of the museum. The museum was established with the mission of bringing aesthetics into everyday life and making art accessible to more people. Tickets are incredibly affordable at just $30, making it a must-visit hidden gem that adds a cultural and artistic vibe to Sanxia Old Street 🫧!\n\n📌 Visitor Information\nContact Number: +886-2-26712009\nOpening Hours:\nMonday to Wednesday: Closed\nThursday to Sunday: 12:00–18:00\n\nLooking to step into a serene, century-old house and immerse yourself in the world of art?\n\nCome and visit the Commoner's Art Museum!")]
                )
            )
        elif text == '庶民美術館紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="庶民美術館三峡老街に隠れるように佇む「庶民美術館」は、老街の3代目である若きアーティスト、呉冠徳さんが創立しました。彼は自然の木の枝を筆🖌️として利用し、驚くほど繊細な油絵を創作しています🎨。彼の作品は「庶民美術館」の見どころの一つです。美術館の設立は、美学を日常生活に取り入れ、多くの人々が芸術の洗礼を受けられることを目指しています。入場料はたったの30元と非常にお手頃で、三峡老街で訪れるべき隠れた名所であり、老街にアートの風情を添えています🫧。\n\n📌 営業情報\n連絡先：+886-2-26712009\n営業時間：\n月曜日～水曜日：休館\n木曜日～日曜日：12:00～18:00\n\n静かな百年の古屋に足を踏み入れ、芸術の洗礼を受けるひとときを味わってみませんか？\n\nぜひ、「庶民美術館」にお越しください！")]
                )
            )
        elif text == '庶民美術館소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="서민 미술관산샤 올드 스트리트에 숨겨진 서민 미술관은 올드 스트리트 3세대 청년 예술가인 \n우관더(吳冠德)가 설립한 곳입니다. 그는 자연에서 얻은 나뭇가지를 붓 🖌️으로 사용하여 놀라울 정도로 섬세한 유화 작품 🎨을 창작하는 데 뛰어난 재능을 가지고 있습니다. 그의 작품은 서민 미술관의 주요 하이라이트 중 하나입니다. 이 미술관은 미학을 일상생활에 녹여내고 더 많은 사람들이 예술의 감화를 받을 수 있도록 하는 취지로 설립되었습니다. 입장료는 단 30대만 원으로 매우 저렴하며, 산샤 올드 스트리트에서 놓쳐서는 안 될 숨은 명소로, 이 거리에 예술적인 분위기를 더해줍니다 🫧.\n\n📌 영업 정보\n연락처: +886-2-26712009\n영업시간:\n월요일~수요일: 휴무\n목요일일요일: 12:00-18:00\n\n고요한 백년 된 고택에서 예술의 향기를 느껴보고 싶으신가요?\n\n그렇다면 서민 미술관에 함께 가보세요!\n")]
                )
            )
        elif text == '花岩山林簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「花岩山林，擁抱自然的每一刻。」\n\n花岩山林是一個結合自然🍃與休閒的景觀園區，園區佔地廣大，分有景觀餐廳🍴、烤肉區🍖與民宿🏨三大區，周邊還有生態魚池🐟、景觀台、櫻花步道🌸、戲水池、天然山泉池、兒童遊戲區、卡拉OK🎤...等。園區周邊擁有壯麗的自然景觀和豐富的生態資源。這裡的特色在於靜謐的山林步道⛰️、壯觀的岩石景觀🪨以及遍布山林間的各種花卉植物，讓每位造訪的旅客都能感受到與自然共處的平和與舒適。\n\n📌營業資訊\n聯絡電話：02-26749618\n營業時間： 全年無休\n星期一-星期五: 9:00-22:00\n星期六-星期日：9:00-23:00\n\n想遠離城市喧囂，擁抱山林的懷抱嗎？\n\n那就來花岩山林，一起展開療癒的自然之旅吧！")]
                )
            )
        elif text == '花岩山林Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Huayan Forest is a scenic park that combines nature 🍃 and leisure. The park spans a vast area and features three main zones: a scenic restaurant 🍴, a barbecue area 🍖, and accommodations 🏨. It also boasts an ecological fish pond 🐟, observation deck, cherry blossom trail 🌸, water play area, natural spring pool, children's playground, karaoke 🎤, and more. Surrounded by stunning natural scenery and rich ecological resources, the park's highlights include tranquil forest trails ⛰️, spectacular rock formations 🪨, and vibrant floral displays, offering every visitor a peaceful and rejuvenating experience in harmony with nature.\n\n📌 Visitor Information\nContact Number: +886-2-26749618\nBusiness Hours: Open Year-Round\nMonday–Friday: 9:00–22:00\nSaturday–Sunday: 9:00–23:00\n\nLooking to escape the hustle and bustle of the city and embrace the serenity of the mountains?\n\nCome to Huayan Forest and embark on a healing journey with nature!")]
                )
            )
        elif text == '花岩山林紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="花岩山林は、自然🍃とレジャーを融合した景観公園です。広大な敷地を有し、景観レストラン🍴、バーベキューエリア🍖、民宿🏨の三つの主要ゾーンがあります。また、生態魚池🐟、展望台、桜の遊歩道🌸、水遊び場、天然山泉プール、子供用遊び場、カラオケ🎤など、多彩な施設も揃っています。周辺は壮大な自然景観と豊富な生態資源に囲まれ、静かな山林の遊歩道⛰️、壮観な岩石景観🪨、そして山林に咲き誇る様々な花々が特色で、訪れるすべての方が自然との共存の平和と快適さを感じられる場所です。\n\n📌 営業情報\n連絡先: +886-2-26749618\n営業時間: 年中無休\n月曜日～金曜日: 9:00～22:00\n土曜日～日曜日: 9:00～23:00\n\n都市の喧騒を離れ、山林の懐に抱かれてみませんか？\n\n花岩山林で、癒しの自然旅を一緒に始めましょう！")]
                )
            )
        elif text == '花岩山林소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="화암산림은 자연🍃과 레저를 결합한 경관 공원입니다. 광활한 부지에 전망 레스토랑🍴, 바비큐 구역🍖, 민박🏨 등 세 가지 주요 구역이 있으며, 생태 어연못🐟, 전망대, 벚꽃 산책로🌸, 물놀이장, 천연 산천수 풀, 어린이 놀이 구역, 노래방🎤 등 다양한 시설도 갖추고 있습니다. 주변은 웅장한 자연 경관과 풍부한 생태 자원으로 둘러싸여 있으며, 고요한 산림 산책로⛰️, 웅장한 바위 경관🪨, 그리고 숲 속에 만개한 꽃들이 이곳의 특징으로, 방문하는 모든 이들에게 자연과의 조화로운 평온함과 편안함을 제공합니다.\n\n📌 영업 정보\n연락처: +886-2-26749618\n영업시간: 연중무휴\n월요일~금요일: 9:00~22:00\n토요일~일요일: 9:00~23:00\n\n도시의 소음을 떠나 산림의 품속에 안겨보지 않으시겠습니까?\n\n화암산림에서 자연과 함께 치유의 여행을 시작하세요!")]
                )
            )
        elif text == '新旺集瓷簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「捏泥巴捏泥巴，捏捏捏捏捏泥巴～」\n\n喜歡創意又有趣的手工藝嗎？新旺集瓷邀你一起探索陶瓷的世界！\n這裡不僅能欣賞台灣獨特的陶瓷藝術，還能親自參加陶藝工作坊，與專業陶藝師一起動手捏泥巴，打造屬於自己的陶瓷藝術品🖼️ 體驗手作的樂趣，帶回的不只是作品，還有滿滿的成就感🥳\n\n📌營業資訊\n聯絡電話：02-2678-9571\n營業時間：\n  星期一、二：休息\n星期三：13:00 - 18:00\n星期四至日：10:00 - 18:00\n\n快來新旺集瓷，開啟你的陶藝創作之旅吧🤩")]
                )
            )
        elif text == '新旺集瓷Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Do you enjoy creative and fun crafts? Xinwang Ceramics invites you to explore the world of pottery! Here, you can not only admire Taiwan's unique ceramic art but also join pottery workshops to create your own ceramic masterpiece under the guidance of professional ceramic artists 🖼️. Experience the joy of handmade art and take home more than just a piece—you’ll leave with a sense of accomplishment 🥳.\n\n📌Operating Information\nContact Number: +886-2-2678-9571\nBusiness Hours:\nMonday & Tuesday: Closed\nWednesday: 1:00 PM - 6:00 PM\nThursday to Sunday: 10:00 AM - 6:00 PM\n\nCome visit Xinwang Ceramics and start your pottery creation journey 🤩!")]
                )
            )
        elif text == '新旺集瓷紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="創意的で楽しい手工芸が好きですか？新旺陶芸工房があなたを陶磁器の世界へご招待します！\nここでは台湾独特の陶磁芸術を鑑賞できるだけでなく、プロの陶芸家と一緒に陶芸ワークショップに参加し、自分だけの陶磁作品を作り上げることができます🖼️。手作りの楽しさを体験し、作品だけでなく達成感もたっぷり持ち帰りましょう🥳。\n\n📌 営業情報\n電話番号：+886-2-2678-9571\n営業時間：\n月曜日・火曜日：定休日\n水曜日：13:00 - 18:00\n木曜日～日曜日：10:00 - 18:00\n\nぜひ新旺陶芸工房に足を運んで、陶芸創作の旅を始めましょう🤩！")]
                )
            )
        elif text == '新旺集瓷소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="창의적이고 재미있는 수공예를 좋아하시나요? 신왕 도자기가 여러분을 도자기의 세계로 초대합니다!\n여기에서는 대만만의 독특한 도자 예술을 감상할 수 있을 뿐만 아니라, 전문 도예가와 함께 도자기 워크숍에 참여하여 나만의 도자기 작품을 만들어볼 수 있습니다🖼️. 손으로 직접 만드는 즐거움을 경험하고, 작품뿐만 아니라 가득 찬 성취감도 함께 가져가세요🥳.\n\n📌 영업 정보\n연락처: +886-2-2678-9571\n영업 시간:\n월요일, 화요일: 휴무\n수요일: 오후 1:00 - 오후 6:00\n목요일~일요일: 오전 10:00 - 오후 6:00\n\n신왕 도자기를 방문하여 도자기 창작 여행을 시작해 보세요🤩!")]
                )
            )
        elif text == '三鶯二橋簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「鈴鈴鈴🔔～帶你騎進鶯歌之眼」\n\n三鶯二橋是台灣的一座公路橋樑，跨越大漢溪、連接新北市三峽區、樹林區與鶯歌區。\n全長1.4公里，因其圓形且特殊的車軌，廣受眾多攝影行家的青睞，有了「鶯歌之眼」的美名。\n無論是熱愛單車旅行的你，還是尋找攝影靈感的旅人，三鶯二橋都值得一訪！帶上相機📷和腳踏車🚴，來捕捉「鶯歌之眼」的壯麗景色，感受騎行於美景中的自在與愜意。歡迎大家前來探索，享受這場結合自然與人文的美好旅程！\n\n📌營業資訊\n聯絡電話：02-29603456\n營業時間：全年開放\n\n想要來一場自然與藝術的碰撞之旅嗎？\n那就來傳說中的鶯歌之眼就對了🤩")]
                )
            )
        elif text == '三鶯二橋Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="San-Ying Second Bridge is a highway bridge in Taiwan that spans the Dahan River, connecting the districts of Sanxia, Shulin, and Yingge in New Taipei City.\nWith a total length of 1.4 kilometers, its circular and unique tracks have earned it the nickname “The Eye of Yingge,” making it a favorite spot among photography enthusiasts.\nWhether you’re a cycling enthusiast or a traveler in search of photography inspiration, the San-Ying Second Bridge is a must-visit destination!\nBring your camera 📷 and bicycle 🚴 to capture the breathtaking scenery of “The Eye of Yingge” and enjoy the freedom and ease of riding through its stunning views.\n\n📌 Operating Information\nContact Number: +886-2-29603456\nOpening Hours: Open year-round\n\nLooking for a journey where nature meets art? \nThen the legendary “Eye of Yingge” is the perfect destination for you 🤩!")]
                )
            )
        elif text == '三鴬二橋紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="日文三鶯二橋は、台湾の公路橋で、大漢渓を跨ぎ、新北市の三峡区、樹林区、鶯歌区を結んでいます。\n全長は1.4キロメートルで、円形の独特なデザインが特徴的なため、「鶯歌の眼」という愛称で知られ、写真愛好家たちに大変人気があります。\nサイクリングを愛するライダーでも、写真のインスピレーションを探している旅人でも、三鶯二橋は訪れる価値のあるスポットです！カメラ 📷 と自転車 🚴 を持って、「鶯歌の眼」の壮大な景色を撮影し、景色の中を自由に駆け抜ける爽快感を味わいましょう。\n\n📌 営業情報\n電話番号：+886-2-29603456\n営業時間：年中無休\n\n自然とアートが出会う旅をしてみませんか？\n伝説の「鶯歌の眼」があなたを待っています 🤩！")]
                )
            )
        elif text == '三鶯二橋소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="삼앵 2교는 대만에 위치한 고속도로 다리로, 다한시를 가로지르며 신베이시의 싼샤구, 술린구, 잉거구를 연결합니다.\n총 길이는 1.4km로, 원형의 독특한 디자인 덕분에 “잉거의 눈”이라는 별칭을 얻었으며, 사진 애호가들 사이에서 큰 인기를 끌고 있습니다.\n사이클링을 사랑하는 라이더든, 사진 촬영의 영감을 찾는 여행자든, 삼앵 2교는 꼭 방문해야 할 명소입니다! 카메라 📷와 자전거 🚴를 챙겨 “잉거의 눈”이 선사하는 웅장한 경관을 담고, 아름다운 풍경 속에서 자유롭게 달리는 즐거움을 만끽해 보세요.\n\n📌 영업 정보\n연락처: +886-2-29603456\n운영 시간: 연중무휴\n\n자연과 예술이 만나는 여행을 떠나고 싶으신가요?\n 전설적인 “잉거의 눈”이 바로 여러분을 기다리고 있습니다 🤩!")]
                )
            )
        elif text == '陶瓷博物館簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「從這裡開始『陶』進你心裡！」\n\n鶯歌陶瓷博物館是全台首座陶瓷主題博物館位於新北市鶯歌區，是台灣首座以陶瓷為主題的專業博物館🏛️。館內展出豐富的陶藝藝術品及文化展覽，不定期還會推出創意特展，充分展現鶯歌產業與在地特色。館外另設陶瓷藝術園區是鶯歌陶瓷博物館的陶瓷主題公園，園區四處綠意盎然，是鶯歌有名的打卡勝地之一📷；夏天時也會開放戲水園區💦，無論大人小孩都很適合到此一遊🥳\n\n📌營業資訊\n聯絡電話： 02-86772727\n營業時間：  \n平日：09:30-17:00\n假日：09:30-18:00\n休館時間：每月第一個星期一\n\n想瞭解陶瓷的文化與歷史嗎？\n想進入陶瓷的藝術世界嗎？\n那就來鶯歌陶瓷博物館吧‼️")]
                )
            )
        elif text == '陶瓷博物館Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The Yingge Ceramics Museum is Taiwan's first ceramic-themed museum, located in the Yingge District of New Taipei City. It is the island's premier professional museum dedicated to ceramics🏛️. The museum features a rich collection of ceramic artworks and cultural exhibitions, with occasional creative special exhibitions, fully showcasing the local industry and feature of Yingge.\nOutside the museum, there is a Ceramic Art Park, a ceramic-themed public park that is one of Yingge's most famous photo spots📷. In summer, the water play area is also open💦, making it a fun destination for both adults and children🥳.\n\n📌 Operating Information\n Contact number: +886-2-86772727\n Hours of Operation:\n Weekdays: 09:30 AM - 5:00 PM\n Weekends: 09:30 AM - 6:00 PM\nClosed: First Monday of every month\n\nInterested in learning about ceramic culture and history?\nWant to enter the world of ceramic art?\nThen come visit the Yingge Ceramics Museum‼️")]
                )
            )
        elif text == '鴬歌陶磁博物館紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=" 鶯歌陶磁器博物館は、台湾初の陶磁器をテーマにした博物館で、新北市鶯歌区に位置しています🏛️。館内では、豊富な陶芸作品や文化展示が行われており、不定期に創造的な特別展示も開催されています。これにより、鶯歌の産業と地域の特色を十分に表現しています。\n館外には陶磁器芸術公園があり、鶯歌陶磁器博物館の陶磁器テーマパークとして広がっています。公園内は緑豊かで、鶯歌で人気のある写真スポットのひとつです📷。夏には水遊びエリアも開放され、子供から大人まで楽しめる場所です💦🥳\n\n📌 営業情報\n連絡先：+886-2-86772727\n営業時間：\n 平日：09:30〜17:00\n休日：09:30〜18:00\n休館日：毎月の第1月曜日\n\n陶磁器の文化や歴史に興味がありますか？\n陶磁器の芸術の世界に入りたいですか？\nそれなら、鶯歌陶磁器博物館にぜひお越しください‼️")]
                )
            )
        elif text == '陶瓷博物館소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌 도자기 박물관은 대만 최초의 도자기 테마 박물관으로, 신베이시 鶯歌구에 위치하고 있습니다🏛️. 이 박물관은 대만에서 유일하게 도자기를 주제로 한 전문 박물관으로, 풍성한 도자기 예술 작품과 문화 전시를 선보이고 있으며, 정기적으로 창의적인 특별 전시도 개최하여 鶯歌의 산업과 지역적 특색을 잘 보여줍니다.\n박물관 외부에는 도자기 예술 공원이 있으며, 鶯歌 도자기 박물관의 도자기 테마 공원으로, 공원 곳곳이 푸르름으로 가득 차 있어 鶯歌의 유명한 포토존 중 하나입니다📷. \n여름에는 물놀이 구역도 개방되어, 어른과 아이 모두 즐기기 좋은 곳입니다💦🥳\n\n📌 운영 정보\n연락처: +886-2-86772727\n운영 시간:\n 평일: 09:30～17:00\n 주말: 09:30～18:00\n 휴관일: 매월 첫 번째 월요일\n\n도자기의 문화와 역사에 대해 배우고 싶나요?\n도자기 예술의 세계로 들어가고 싶나요?\n그렇다면, 鶯歌 도자기 박물관에 꼭 방문해 보세요‼️")]
                )
            )
        elif text == '光點藝術中心簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「一閃一閃亮晶晶~ 滿天都是小星星~」✨\n\n你以為的光點藝術中心是像夜空中一閃一閃的星星嗎🌌？\n不！\n光點藝術中心結合了藝術、活動、展覽、文創、生活、食趣等六大特色，每個月也會精心規劃藝術展覽及特別企劃活動，除了欣賞多元藝術外，更可以開拓視野，無論是是欣賞精美藝品🎨，或是選購伴手好禮🎁，都能給旅客帶來豐富多元的選擇！🤩\n\n📌營業資訊\n聯絡電話：02-2678-9599\n星期一-星期日：10:00-19:00\n\n想一次體驗多種不同樂趣嗎？🎨🛍️🖼️✨\n鶯歌光點藝術中心絕對是你的最佳首選！")]
                )
            )
        elif text == '光點藝術中心Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Do you think the Spot Handcraft Gallery is like twinkling stars in the night sky?\nNo!\nThe Spot Handcraft Gallery combines six key features: art, activities, exhibitions, cultural creativity, lifestyle, and culinary delights. Every month, it carefully curates art exhibitions and special events. Beyond enjoying diverse forms of art, visitors can broaden their horizons. Whether you're admiring exquisite artworks 🎨 or shopping for unique gifts 🎁, this destination offers a rich variety of experiences for all! 🤩\n\n📌 Operating Information\nContact Number: +886-2-2678-9599\nMonday–Sunday: 10:00 AM–7:00 PM\n\nLooking to experience various kinds of fun in one go? 🎨🛍️🖼️✨\nSpot Handcraft Gallery is your best choice!")]
                )
            )
        elif text == '光點藝術中心紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="夜空の星のように光点芸術センターも輝いていると思いますか？\nいいえ！\n光点芸術センターは、芸術、イベント、展示、文創、生活、食趣の6つの特徴を融合しています。毎月、精選された芸術展や特別企画イベントを開催し、多様な芸術を楽しむだけでなく、視野を広げることができます。精巧な芸術品を鑑賞したり🎨、特別なお土産を購入したり🎁、訪れる人々に多彩な選択肢を提供します！🤩\n\n📌 営業情報\n電話番号：+886-2-2678-9599\n営業時間：月曜日～日曜日 10:00～19:00\n\n多様な楽しみを一度に体験したい方へ🎨🛍️🖼️✨\n鶯歌光点芸術センターは間違いなく最高の選択です！")]
                )
            )
        elif text == '光點藝術中心소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="빛점예술센터도 밤하늘의 별처럼 반짝이는 곳일까요?\n아니요!\n빛점예술센터는 예술, 활동, 전시, 문화 창작, 라이프스타일, 미식 등 여섯 가지 특징을 결합한 공간입니다. 매달 정성껏 기획한 예술 전시와 특별 이벤트를 선보이며, 다양한 예술 감상뿐만 아니라 시야를 넓힐 기회를 제공합니다. 정교한 예술 작품 감상 🎨, 혹은 특별한 선물을 구매 🎁 등 다양한 즐거움을 선사합니다! 🤩\n\n📌 운영 정보\n연락처: +886-2-2678-9599\n운영 시간: 월요일일요일 10:0019:00\n\n다양한 재미를 한 번에 경험하고 싶으신가요? 🎨🛍️🖼️✨\n잉거 빛점예술센터는 최고의 선택입니다!")]
                )
            )
        elif text == '三鶯之心空間藝術特區簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「無痛出國～彷彿置身美國大峽谷🏜️！」\n\n三鶯之心空間藝術特區，位於三鶯藝術村的戶外草地，緊鄰新北市美術館🕌，其中最吸引人的就是15公尺高的《坯》藝術裝置，走進坯中就彷彿置身在美國羚羊谷一樣，還可循著旋轉樓梯登頂，以360度視角遠眺鶯歌、三峽風光，周末吸引許多民眾前來美拍📷，不論室內室外都能拍出不同的好光彩！😍\n\n📌營業資訊\n聯絡電話：02-29603456\n營業時間：全年無休\n開放參觀時間：星期六、日 13:30-16:30\n\n想體驗一次巨人國的世界嗎?🗿\n那就跟我們一起到三鶯之心看看吧！")]
                )
            )
        elif text == '三鶯之心空間藝術特區Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The 'Heart of San-Ying' Space Art Zone, located in the outdoor grass field of San-Ying Art Village and adjacent to the New Taipei City Art Museum 🕌, boasts the stunning 15-meter-tall 'Clay' art installation. Walking into 'Clay' feels like stepping into the Antelope Canyon in the U.S. You can also climb the spiral staircase to the top and enjoy a 360-degree panoramic view of Yingge and Sanxia. Every weekend, the area draws crowds eager to capture breathtaking photos 📷. Indoors or outdoors, every angle shines differently! 😍\n\n📌 Operating Information\nContact Number: +886-2-29603456\nOpening Hours: Open Year-Round\nVisiting Hours: Saturdays & Sundays, 1:30 PM–4:30 PM\n\nWant to experience a world made for giants? 🗿\nJoin us at the 'Heart of San-Ying' to see it for yourself!")]
                )
            )
        elif text == '三鶯之心空間藝術特區紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="三鶯之心スペースアートゾーンは、三鶯芸術村の屋外芝生広場に位置し、新北市立美術館🕌に隣接しています。中でも最も注目を集めているのは、高さ15メートルのアートインスタレーション「坯（クレイ）」。この中に入ると、まるでアメリカのアンテロープキャニオンにいるかのような感覚を味わえます。また、らせん階段を登れば、鶯歌と三峡の絶景を360度パノラマビューで堪能できます。週末には多くの人々がフォトジェニックなスポットを求めて訪れます📷。屋内でも屋外でも、どこでも素敵な写真が撮れます！😍\n\n📌 営業情報\n電話番号：+886-2-29603456\n営業時間：年中無休\n公開時間：土曜・日曜 13:30～16:30\n\n巨人の国にいるような体験をしたいですか？🗿\nぜひ「三鶯之心」に遊びに来てください！")]
                )
            )
        elif text == '三鶯之心空間藝術特區소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="삼잉의 심장 공간 예술 특구는 삼잉 예술촌 야외 잔디밭에 위치하고 있으며, 신베이시 미술관 🕌 옆에 자리 잡고 있습니다. 그중 가장 매력적인 것은 15미터 높이의 '클레이(坯)' 예술 설치물입니다. '클레이' 안으로 들어가면 마치 미국 앤텔로프 캐니언에 온 것 같은 기분을 느낄 수 있습니다. 또한, 나선형 계단을 따라 꼭대기에 올라가면 360도 전경으로 잉거와 산샤의 풍경을 감상할 수 있습니다. 주말이면 많은 사람들이 멋진 사진 📷을 찍기 위해 이곳을 찾습니다. 실내외 어디서든 특별한 빛을 담아낼 수 있습니다! 😍\n\n📌 운영 정보\n연락처: +886-2-29603456\n운영 시간: 연중무휴\n관람 시간: 토요일,일요일13:30~16:30\n\n거인국의 세계를 체험해보고 싶으신가요? 🗿\n그렇다면 삼잉의 심장으로 함께 떠나보세요!")]
                )
            )
        elif text == '新北市美術館簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「蘆葦叢中的當代藝術殿堂🏛️」\n\n新北市美術館外牆立面靈感擷取三鶯河岸常見的「蘆葦」作為轉譯，透過高低錯落變化的噴砂管，詮釋出「蘆葦」隨風搖曳的意象🍃。館內設有藝術街坊、圓頂藝術空間、戶外園區等設施，夏季時更會開放戲水沙坑供訪客遊玩💦。除了白天的景緻，這座美術館越夜越美🌃。其燈光設計也是一大重點，高低錯落變化的噴砂管在室內燈光照射下，又是另一幅美景，無論白天或夜晚都有不同的光景供大家參觀！🤩\n\n📌營業資訊\n聯絡電話：02-26796088\n營業時間：星期二至星期日　10:00-17:00\n休館時間：星期一\n\n想體驗當代藝術美學嗎?🏛️\n那就來新北市美術館看看吧！")]
                )
            )
        elif text == '新北市美術館Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The façade of the New Taipei City Art Museum draws inspiration from the iconic reeds along the San-Ying River. Through sandblasted pipes of varying heights, it captures the swaying imagery of reeds in the wind 🍃. Inside, visitors can explore diverse spaces like the Art Street, the Dome Art Space, and the Outdoor Garden. During summer, a water play area with sand pits is also open for extra fun 💦.\nThe museum’s beauty transcends time, as it transforms into a luminous spectacle at night 🌃. The unique lighting design highlights the textured pipes, offering a completely different visual experience from day to night. Whether under the sun or the stars, every visit promises a new perspective! 🤩\n\n📌 Visitor Information\nContact: +886-2-26796088\nHours: Tuesday to Sunday, 10:00 AM–5:00 PMClosed: Mondays\n\nImmerse yourself in the beauty of contemporary art—visit the New Taipei City Art Museum ! 🏛️")]
                )
            )
        elif text == '新北市美術館紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="新北市美術館の外壁デザインは、三鶯河沿いでよく見られる「蘆葦」からインスピレーションを受けています。高低差のあるサンドブラスト加工のパイプを使用して、風に揺れる蘆葦の姿を美しく表現しました 🍃。館内には、アートストリート、ドーム型アート空間、屋外ガーデンなど、多彩な施設が揃っています。夏季には、水遊びと砂場も開放され、訪れる人々に楽しみを提供します 💦。\nこの美術館は昼だけでなく、夜も魅力的です 🌃。照明デザインにも注力しており、サンドブラストパイプに照明が映し出されると、まるで別世界のような美しさを楽しめます。昼と夜、それぞれ異なる景色を満喫してください！ 🤩\n\n📌 営業情報\n電話番号： +886-2-26796088\n開館時間：火曜日～日曜日 10:00～17:00\n休館日：月曜日\n\n現代アートの魅力を体験しに、新北市美術館へお越しください！ 🏛️")]
                )
            )
        elif text == '新北市美術館소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="신베이시 미술관의 외벽은 삼잉 강변의 대표적인 풍경인 갈대에서 영감을 받았습니다. 높낮이가 다른 샌드블라스트 파이프를 통해 바람에 흔들리는 갈대의 모습을 아름답게 표현했습니다 🍃. 미술관 내부에는 예술 거리, 돔 아트 스페이스, 야외 정원 등 다양한 시설이\n마련되어 있습니다. 여름에는 물놀이와 모래밭이 개방되어 방문객들에게 즐거움을 선사합니다 💦.\n이 미술관은 낮뿐만 아니라 밤에도 특별한 매력을 선사합니다 🌃. 조명 디자인이 돋보이며, 샌드블라스트 파이프에 비친 빛은 마치 꿈같은 풍경을 연출합니다. 낮과 밤, 각각의 아름다움을 만끽해 보세요! 🤩\n\n📌 운영 정보\n연락처:  +886-2-26796088\n운영 시간: 화요일일요일 오전 10시오후 5시\n휴관일: 월요일\n\n현대 예술의 아름다움을 느끼고 싶다면, 신베이시 미술관으로 오세요! 🏛️")]
                )
            )
        elif text == '河南砂鍋手工扯麵簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人氣三峽美食推薦！👍\n河南手工扯麵生意超好，內用外帶都是滿滿的排隊人潮\n菜單必點番茄蛋砂鍋扯麵，每樣食材的組合都很到位\n推薦大家如果來到三峽的話，別只是在三峽老街走走，可以到稍遠一點的地方吃碗美味的河南手工扯麵！🍜\n\n📌營業資訊\n平日：　10:30-20:30 (星期四休息)\n假日：　10:30-20:30")]
                )
            )
        elif text == '河南砂鍋手工扯麵Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Highly Recommended Three Gorges Food! 👍\nHenan Handmade Noodles is incredibly popular, with long lines for both dine-in and takeout.\nA must-try on the menu is the Tomato Egg Claypot Noodles. Every ingredient is perfectly combined.\nIf you visit Sanxia, don’t just walk around the Old Street—make sure to visit this spot a bit further to enjoy a delicious bowl of Henan Handmade Noodles! 🍜\n\n📌 Business Hours\nWeekdays: 10:30 AM - 8:30 PM (Closed on Thursdays)\nWeekends: 10:30 AM - 8:30 PM")]
                )
            )
        elif text == '河南砂鍋手工扯麵紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="三峡の超人気グルメおすすめ！ 👍\n河南手工扯麵はとても人気があり、店内でもテイクアウトでも長い行列ができます。\nメニューで絶対に試してほしいのは「トマト卵土鍋麺」。すべての食材の組み合わせが完璧です。\n三峡に来た際は、三峡老街だけではなく、少し遠くにある河南手工扯麵で美味しい一杯を是非お楽しみください！🍜\n\n📌 営業時間\n平日：10:30～20:30（木曜日定休）\n週末：10:30～20:30")]
                )
            )
        elif text == '河南砂鍋手工扯麵소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="초인기 삼협 맛집 추천! 👍\n허난 수제 찢어진 면은 매우 인기가 많아서, 매장 안에서나 포장 주문에서도 항상 긴 줄이 서 있습니다.\n메뉴에서 꼭 먹어야 할 것은 '토마토 계란 냄비면'입니다. 모든 재료의 조화가 정말 잘 맞습니다.\n삼협에 오면 삼협 올드스트리트를 걷는 것만으로 끝내지 말고, 조금 더 멀리 가서 맛있는 허난 수제 찢어진 면 한 그릇을 즐겨 보세요! 🍜\n\n📌 영업 시간\n평일: 10:30 AM - 8:30 PM (목요일 휴무)\n주말: 10:30 AM - 8:30 PM")]
                )
            )
        elif text == '真本家雞蛋糕簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="三峽老街除了傳統的金牛角之外，還有一間絕對不能錯過的美食「真本家」。\n這裡的「真角燒」是一款可愛的金牛角造型雞蛋糕🥐，當熱騰騰的雞蛋糕剛出爐時，香氣四溢，瞬間充滿整個空氣。特別推薦香酥外皮包裹著濃郁牽絲起司的雞蛋糕🧀，外脆內軟，風味絕佳！更有期間限定的怦然心動口味，讓人欲罷不能🤤。\n\n📌營業資訊\n星期一-星期二：休息\n星期三-星期日：12:00-17:30")]
                )
            )
        elif text == '真本家雞蛋糕Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Aside from the traditional croissant, Sanxia Old Street also has a must-try delicacy, 'Zhen Ben Jia.'\nTheir 'Zhen Jiao Shao' is an adorable golden bull-shaped egg cake 🥐. When the egg cake is freshly baked, its fragrance fills the air, instantly tempting everyone. Highly recommended is the crispy exterior with a rich, cheesy, stringy filling 🧀—crispy on the outside and soft on the inside, absolutely delicious! They also offer a limited-time 'Heart-throbbing' flavor that will leave you craving more 🤤.\n\n📌 Business hours:\nMonday-Tuesday: Closed\nWednesday-Sunday: 12:00 PM - 5:30 PM")]
                )
            )
        elif text == '真本家雞蛋糕紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="三峡老街では、伝統的な金牛角のほかに、「真本家」という絶対に見逃せない美味しい店があります。\nこちらの「真角焼き」は、可愛らしい金牛角型のたまごケーキ🥐です。焼きたてのたまごケーキは香りが広がり、瞬時に空気を満たします。特におすすめは、サクサクした外皮に濃厚で糸を引くチーズが包まれたたまごケーキ🧀。外はカリカリ、内はふわふわで、絶品です！さらに、期間限定の「心躍る」フレーバーもあり、もう一口がやめられません🤤。\n\n📌 営業時間：\n月曜日〜火曜日：休業\n水曜日〜日曜日：12:00 - 17:30")]
                )
            )
        elif text == '真本家雞蛋糕소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="삼협 올드스트리트에서는 전통적인 금우각 외에도, 절대 놓칠 수 없는 미식 명소인 '진본가'가 있습니다.\n여기서의 '진각구이'는 귀여운 금우각 모양의 계란빵🥐입니다. 갓 구운 계란빵에서 퍼지는 향기가 공기 중에 가득 차며, 모든 이들을 유혹합니다. 특히 추천하는 것은 바삭한 겉면에 진하고 늘어나는 치즈가 듬뿍 들어간 계란빵🧀으로, 겉은 바삭하고 속은 부드러워 정말 맛있습니다! 또한, 기간 한정으로 제공되는 '심쿵' 맛도 있어, 먹을 때마다 더 먹고 싶어질 거예요 🤤.\n\n📌 영업시간:\n월요일화요일: 휴무\n수요일일요일: 12:00 PM - 5:30 PM")]
                )
            )
        elif text == '鄭記古早味豬血糕簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人氣三峽美食推薦！\n豬血糕一拿到手就聞到花生香！豬血糕沾刷一層特調蒜醬，再沾附上滿滿花生粉🥜與香菜點綴，這豬血糕沒什麼辣感，連小孩都敢吃✔️，辣醬只是提香點辣而已，重口味豬血糕特別耐吃，又Q又軟的口感搭配醬汁的味道跟花生的香氣，吃完感覺意猶未盡🤤！\n\n📌營業資訊\n平日：11:00-18:00 (星期二休息)\n假日：11:00-18:00")]
                )
            )
        elif text == '鄭記古早味豬血糕Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Highly popular Sanxia food recommendation!\nAs soon as you hold the pig blood cake, the peanut aroma hits you! The pig blood cake is brushed with a special garlic sauce, then coated with a generous amount of peanut powder 🥜 and garnished with cilantro. This pig blood cake isn’t very spicy, making it perfect for kids ✔️. The spicy sauce just adds a hint of fragrance and a little kick. The rich and flavorful pig blood cake is chewy and soft, and the combination of the sauce and peanut aroma leaves you wanting more 🤤!\n\n📌 Business hours:\nWeekdays: 11:00 AM - 6:00 PM (Closed on Tuesdays)\nWeekends: 11:00 AM - 6:00 PM")]
                )
            )
        elif text == '鄭記古早味豬血糕紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人気の三峡美食おすすめ！\n豚血ケーキを手に取ると、花生の香りが広がります！豚血ケーキには特製のガーリックソースが塗られ、その後、たっぷりの花生粉🥜と香菜がトッピングされています。この豚血ケーキは辛さが控えめで、子供でも食べやすい✔️。辛いソースは香りを引き立て、少しだけ辛味を加えています。濃い味の豚血ケーキは特に食べ応えがあり、モチモチと柔らかい食感がソースの味や花生の香りと相性抜群で、食べ終わった後もまだ食べ足りない気分になります🤤！\n\n📌 営業時間：\n平日：11:00 - 18:00（火曜日定休）\n週末：11:00 - 18:00")]
                )
            )
        elif text == '鄭記古早味豬血糕소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="대인기 삼협 맛집 추천!\n돼지피떡을 손에 쥐자마자 땅콩 향이 퍼집니다! 돼지피떡에 특제 마늘 소스를 바르고, 그 위에 듬뿍 땅콩가루🥜와 고수가 얹혀 있습니다. 이 돼지피떡은 매운 맛이 강하지 않아 아이들도 쉽게 먹을 수 있어요✔️. 매운 소스는 향을 돋우고 살짝 매운 맛을 더하는 정도입니다. 진한 맛의 돼지피떡은 씹는 맛이 좋고 부드러우며, 소스와 땅콩의 향이 잘 어우러져 먹고 난 후에도 여운이 남습니다🤤!\n\n📌 영업시간:\n평일: 11:00 AM - 6:00 PM (화요일 휴무)\n주말: 11:00 AM - 6:00 PM")]
                )
            )
        elif text == '山泉水手工豆花店簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人氣三峽美食推薦！👍\n全台唯一三峽山泉水豆花，不管平日假日，白天或黑夜總可見排隊人潮👥，三峽超人氣排隊豆花店，使用非基因改造黃豆，超人氣口味是粉圓豆花、雪蓮子豆花，真材實料，豆花扎實細緻綿密☁️，帶有彈性，滿滿豆香，值得品嚐看看！\n\n📌營業資訊\n每日：9:00-22:00")]
                )
            )
        elif text == '山泉水手工豆花店Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Highly popular Sanxia food recommendation! 👍\nThe only Sanxia mountain spring water tofu pudding in Taiwan! Whether it’s a weekday or weekend, day or night, there’s always a line of customers 👥. This super popular tofu pudding shop in Sanxia uses non-GMO soybeans. The most popular flavors are tapioca tofu pudding and snow lotus seed tofu pudding. Made with real ingredients, the tofu pudding is dense, smooth, and creamy ☁️, with a springy texture and rich soy flavor. It’s definitely worth a try!\n\n📌 Business hours:\nDaily: 9:00 AM - 10:00 PM")]
                )
            )
        elif text == '山泉水手工豆花店紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人気の三峡美食おすすめ！👍\n台湾唯一の三峡山の湧水を使った豆花！平日でも休日でも、昼夜問わず行列ができる人気の豆花店です👥。三峡で超人気の豆花店は、遺伝子組み換えでない大豆を使用しています。特に人気の味はタピオカ豆花と雪蓮子豆花です。素材本来の味が活きており、豆花はしっかりとした食感で、滑らかでクリーミー☁️、弾力があり、豊かな豆の香りが広がります。ぜひ一度味わってみてください！\n\n📌 営業時間：\n毎日：9:00 - 22:00")]
                )
            )
        elif text == '山泉水手工豆花店소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="대인기 삼협 맛집 추천! 👍\n전국에서 유일한 삼협 산泉수 두부 푸딩! 평일이나 주말, 낮이나 밤에 언제나 줄을 서는 사람들👥. 삼협에서 인기 있는 두부 푸딩 가게는 비유전자조작 대두를 사용합니다. 가장 인기 있는 맛은 타피오카 두부 푸딩과 설련자 두부 푸딩입니다. 진짜 재료로 만든 두부 푸딩은 탄탄하고 부드럽고 촉촉☁️, 쫄깃한 식감과 고소한 대두 향이 가득합니다. 꼭 한 번 맛보세요!\n\n📌 영업시간:\n매일: 9:00 AM - 10:00 PM")]
                )
            )
        elif text == '來來滷味簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人氣三峽美食推薦！👍\n百年老宅裡品嚐蔬果熬煮高湯添加中藥滷製的來來滷味，以新鮮蔬食和豆製品為主的輕食料理，健康無負擔，清香的中藥香氣，搭配新鮮蔬果的鮮甜🥦，簡單卻極具滋味；價格也十分親民，是銅板價🪙就可以享受的美食料理🤩！\n\n📌營業資訊\n星期二-星期三：休息\n星期一、星期四-星期五：12:30-18:00\n星期六-星期日：11:00-19:00")]
                )
            )
        elif text == '來來滷味Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Highly popular Sanxia food recommendation! 👍\nSavor 'Lai Lai Braised Delicacies' in a century-old house, where the broth is made with vegetables and fruits and infused with Chinese herbs. This light meal focuses on fresh vegetables and soy-based products, offering a healthy and guilt-free option. The subtle aroma of Chinese herbs pairs beautifully with the natural sweetness of fresh vegetables and fruits 🥦. Simple yet incredibly flavorful! The prices are very affordable, allowing you to enjoy this delicious meal for just pocket change 🪙🤩.\n\n📌 Business hours:\nTuesday-Wednesday: Closed\nMonday, Thursday-Friday: 12:30 PM - 6:00 PM\nSaturday-Sunday: 11:00 AM - 7:00 PM")]
                )
            )
        elif text == '來來滷味紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人気の三峡美食おすすめ！👍\n百年の古民家で味わう「来来滷味」は、野菜や果物で煮込んだスープに中薬で味付けした一品です。新鮮な野菜と大豆製品を中心とした軽食料理で、ヘルシーかつ負担の少ない選択です。中薬のほのかな香りが、新鮮な野菜や果物の自然な甘み🥦と絶妙にマッチします。シンプルながら非常に味わい深い！価格もとてもリーズナブルで、手軽に楽しめる美味しい料理です🪙🤩。\n\n📌 営業時間：\n火曜日〜水曜日：休業\n月曜日・木曜日〜金曜日：12:30 - 18:00\n土曜日〜日曜日：11:00 - 19:00")]
                )
            )
        elif text == '來來滷味소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="대인기 삼협 맛집 추천! 👍\n100년 된 고택에서 즐기는 '라이라이 졸미'는 채소와 과일로 끓인 육수에 한약재로 맛을 낸 요리입니다. 신선한 채소와 두부 제품을 중심으로 한 가벼운 식사로, 건강하고 부담 없는 선택입니다. 은은한 한약재 향이 신선한 채소와 과일의 자연스러운 단맛🥦과 조화를 이루며, 심플하면서도 깊은 맛을 선사합니다. 가격 또한 매우 합리적이며, 주머니돈으로도 즐길 수 있는 요리입니다🪙🤩.\n\n📌 영업시간:\n화요일수요일: 휴무\n월요일, 목요일금요일: 12:30 PM - 6:00 PM\n토요일~일요일: 11:00 AM - 7:00 PM")]
                )
            )
        elif text == 'MERLIN.M梅林麵簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人氣三峽美食推薦！👍\n你以為MERLIN.M是網美咖啡廳嗎\n不❌\n其實它是間低調雅緻拉麵店🍜，梅林麵店販售各式台式口味的拉麵和乾拌麵，也有超下飯的麻婆豆腐飯和各式小菜🥗，很多都是熟悉的菜色，不過在這樣的環境享用，也是全新的體驗～\n\n📌營業資訊\n星期一：休息\n星期二、星期四-星期日：11:30-14:00 17:30-20:00\n星期三：11:30-14:00")]
                )
            )
        elif text == 'MERLIN.M梅林麵Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Highly popular Sanxia food recommendation! 👍\nThink MERLIN.M is an Instagrammable café?\nNot at all! ❌\nIn fact, it’s a low-key and elegant ramen shop 🍜. Merlin Noodle House offers various Taiwanese-style ramen and dry noodles, as well as hearty dishes like mapo tofu rice and a variety of side dishes 🥗. Many of the dishes are familiar favorites, but enjoying them in such a refined setting is a brand-new experience.\n\n📌 Business hours:\nMonday: Closed\nTuesday, Thursday-Sunday: 11:30 AM - 2:00 PM, 5:30 PM - 8:00 PM\nWednesday: 11:30 AM - 2:00 PM")]
                )
            )
        elif text == 'MERLIN.M梅林麵紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="超人気の三峡美食おすすめ！👍\nMERLIN.Mは映えカフェだと思っていませんか？\n実は違います！❌\nここは、控えめで上品な雰囲気のラーメン店🍜です。梅林麺店では、台湾風のラーメンや汁なし麺をはじめ、麻婆豆腐ご飯や各種小皿料理🥗などのご飯が進むメニューを提供しています。どれも馴染みのある料理ですが、このような洗練された空間で味わうのは新鮮な体験になること間違いなしです。\n\n📌 営業時間：\n月曜日：休業\n火曜日・木曜日～日曜日：11:30 - 14:00、17:30 - 20:00\n水曜日：11:30 - 14:00")]
                )
            )
        elif text == 'MERLIN.M梅林麵소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="대인기 삼협 맛집 추천! 👍\nMERLIN.M이 인스타용 카페라고 생각하셨나요?\n전혀 아니에요! ❌\n사실, 여기는 세련되고 우아한 라면 가게입니다 🍜. 멀린 면집에서는 대만식 라면과 비빔면을 비롯해 마파두부 덮밥과 다양한 반찬 🥗을 판매합니다. 대부분 익숙한 메뉴이지만, 이렇게 세련된 분위기에서 즐기는 것은 새로운 경험이 될 것입니다.\n\n📌 영업시간:\n월요일: 휴무\n화요일, 목요일~일요일: 11:30 AM - 2:00 PM, 5:30 PM - 8:00 PM\n수요일: 11:30 AM - 2:00 PM")]
                )
            )

        elif text == 'ESUWA肉桂卷專売處簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="神秘肉桂捲ESUWA 肉桂卷&可頌專売處🥐藏身在三樓，從星巴克旁邊的入口進入，搭乘電梯上三樓即可抵達，等待電梯的同時就聞到陣陣香氣。肉桂捲以3種香、甜、溫潤的肉桂搭配，烤後再抹上濃郁的檸檬糖霜🍋，軟綿香甜，口口滿足🤤，到鶯歌時不妨也順帶一份美味的肉桂捲吧！\n\n📌營業資訊\n每日：11:00-18:00")]
                )
            )
        elif text == 'ESUWA肉桂卷專売處Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Mystical Cinnamon Rolls at ESUWA 🥐A hidden gem on the third floor! Enter through the entrance next to Starbucks and take the elevator to the third floor, where you’ll already start to smell the enticing aroma while waiting for the lift. The cinnamon rolls are made with a blend of three types of cinnamon—fragrant, sweet, and warm—and baked to perfection before being topped with rich lemon icing 🍋. Soft, sweet, and utterly satisfying with every bite 🤤. If you’re visiting Yingge, don’t forget to grab a delicious cinnamon roll!\n\n📌 Business hours:\nDaily: 11:00 AM - 6:00 PM")]
                )
            )
        elif text == 'ESUWA肉桂卷專売處紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="神秘的なシナモンロール「ESUWA」 🥐3階に隠れた名店！スターバックス横の入口から入り、エレベーターで3階へ向かうと、待つ間にも漂う香りが楽しめます。シナモンロールは、香り高く甘く温かみのある3種類のシナモンを使用し、焼き上げた後に濃厚なレモンアイシング🍋を塗っています。柔らかく甘く、口にするたびに満足感でいっぱいに🤤。鶯歌を訪れる際には、ぜひこの美味しいシナモンロールもお持ち帰りください！\n\n📌 営業時間：\n毎日：11:00 - 18:00")]
                )
            )
        elif text == 'ESUWA肉桂卷專売處소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="신비로운 시나몬 롤 ESUWA 🥐3층에 숨겨진 보석 같은 가게! 스타벅스 옆 입구로 들어가 엘리베이터를 타고 3층으로 올라가면, 기다리는 동안부터 향긋한 냄새가 퍼집니다. 시나몬 롤은 향기롭고 달콤하며 따뜻한 느낌을 주는 3종류의 시나몬을 사용해 구워진 후, 진한 레몬 아이싱🍋이 발라져 있습니다. 부드럽고 달콤하며 한 입 한 입이 만족스럽습니다 🤤. 잉거를 방문할 때 이 맛있는 시나몬 롤도 꼭 챙겨가세요!\n\n📌 영업시간:\n매일: 11:00 AM - 6:00 PM")]
                )
            )
        elif text == '阿婆壽司簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="阿婆壽司是鶯歌在地神級小吃，就像我們去嘉義會去吃雞肉飯的道理一樣，在地開賣超過40多年，24小時經營從攤車賣到整棟店面，菜單菜色選項多元，有著各式壽司🍣、關東煮🍢、涼麵🍝，重點是價格非常便宜，完全不用考慮價格💰，想吃什麼直接點下去就對了！\n\n📌營業資訊\n全年無休🆓")]
                )
            )
        elif text == '阿婆壽司Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Grandma’s Sushi is a legendary local snack spot in Yingge. It’s just like how people must try chicken rice when visiting Chiayi—it’s a must! Operating for over 40 years, this 24-hour eatery has grown from a street cart to a full-fledged storefront. The menu offers a wide variety of options, including sushi 🍣, oden 🍢, and cold noodles 🍝. Best of all, the prices are incredibly affordable—you don’t even need to think about the cost 💰. Just order whatever you feel like eating!\n\n📌 Business hours:\nOpen 24/7, year-round 🆓")]
                )
            )
        elif text == '阿婆壽司紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="阿婆寿司は鶯歌の地元で伝説的なスナックスポットです。嘉義で鶏肉飯を食べるように、鶯歌に来たら絶対に試したい一品！40年以上営業を続け、24時間営業のこの店は、屋台から始まり今では店舗として展開されています。メニューは寿司🍣、おでん🍢、冷麺🍝など、豊富な選択肢があります。しかも、価格が非常にリーズナブルで、値段を気にせず好きなものを自由に注文できます💰！\n\n📌 営業時間：\n年中無休、24時間営業 🆓")]
                )
            )
        elif text == '阿婆壽司소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="할머니 스시는 잉거 지역의 전설적인 간식 맛집입니다. 마치 치아이에서 닭고기 덮밥을 먹는 것처럼 잉거에 오면 반드시 먹어봐야 하는 곳입니다! 40년 넘게 영업해온 이곳은 24시간 운영되며, 노점에서 시작해 현재는 가게 전체로 확장되었습니다. 메뉴는 스시 🍣, 오뎅 🍢, 냉면 🍝 등 다양하며, 무엇보다 가격이 매우 저렴해 가격 걱정 없이 먹고 싶은 대로 주문하면 됩니다 💰!\n\n📌 영업시간:\n연중무휴, 24시간 운영 🆓")]
                )
            )
        elif text == '甕仔麵簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="在這家以老倉庫古樸風格設計的餐廳裡，顧客們紛紛享用著店家特別推出的「甕仔麵」，以鶯歌在地生產的陶甕盛裝，為餐點更添一抹懷舊氛圍🏮。古早味的美食與懷舊的氛圍相得益彰，其中「甕仔海鮮麵」更是必點之選，堪稱CP值爆表的一碗麵！品嚐過一次的人，無不對這碗海鮮麵讚不絕口。豐富的配料包括鮮蝦🦐、花枝、魷魚🦑、魚肉🐟與蛤蜊，料多實在，每一口都充滿海洋的鮮味。麵條Q彈爽滑，湯頭則是清爽不油膩，讓人忍不住一口接一口地喝不停🤤。這裡的海鮮麵，絕對值得一試！\n\n📌營業資訊\n平日：11:00-16:00\n假日：11:00-19:00")]
                )
            )
        elif text == '甕仔麵Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="In this restaurant, designed with the rustic charm of an old warehouse 🏮, customers savor the restaurant's special 'Clay Pot Noodles,' served in locally made Yingge ceramic pots. This unique touch adds a nostalgic vibe to the dining experience. The classic flavors perfectly match the retro atmosphere, and the 'Clay Pot Seafood Noodles' are a must-try, offering unbeatable value for money!\nEveryone who has tasted it praises this seafood noodle dish. It comes packed with ingredients like fresh shrimp 🦐, cuttlefish, squid 🦑, fish 🐟, and clams, delivering a rich taste of the ocean in every bite. The noodles are springy and smooth, while the broth is light and non-greasy, making it impossible to stop sipping 🤤. This seafood noodle dish is a culinary experience you won't want to miss!\n\n📌 Business Hours:\nWeekdays: 11:00 AM - 4:00 PM\nWeekends: 11:00 AM - 7:00 PM")]
                )
            )
        elif text == '甕仔麵紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="このレストランは、古い倉庫をイメージした素朴なデザインが特徴🏮で、訪れた人々は地元・鶯歌で作られた陶製の甕（かめ）に盛り付けられた特製「甕仔麺」を堪能しています。この工夫により、懐かしさがさらに引き立ちます。昔懐かしい味わいとレトロな雰囲気が見事に調和しており、中でも「甕仔海鮮麺」は必食の一品で、そのコストパフォーマンスには驚かされます！\n一度でも味わった人は、この海鮮麺を大絶賛します。鮮度抜群のエビ🦐、イカ🦑、スルメ、魚🐟、アサリなどがたっぷりと盛り付けられ、海の幸が満喫できます。麺はモチモチとした食感で、スープはあっさりとして脂っこさがなく、ついつい飲み続けてしまう美味しさ🤤。この海鮮麺は絶対に試してみる価値があります！\n\n📌 営業時間：\n平日：11:00 - 16:00\n週末：11:00 - 19:00")]
                )
            )
        elif text == '甕仔麵소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="이 레스토랑은 옛 창고의 소박한 매력을 살린 디자인이 특징🏮으로, 손님들은 잉거 지역에서 생산된 도자기 항아리에 담긴 특별한 '항아리 국수'를 즐기고 있습니다. 이 독특한 연출은 식사에 추억을 더해줍니다. 전통적인 맛과 복고풍 분위기가 완벽하게 어우러져 있으며, 특히 '항아리 해산물 국수'는 반드시 먹어봐야 할 메뉴로, 가성비가 뛰어납니다!\n한 번 맛본 사람들은 이 해산물 국수를 극찬합니다. 신선한 새우🦐, 오징어🦑, 갑오징어, 생선🐟, 조개 등 다양한 재료가 풍성하게 들어가 있어 바다의 풍미를 한껏 느낄 수 있습니다. 면은 쫄깃하고 부드러우며, 국물은 담백하고 기름지지 않아 계속해서 마시게 되는 맛🤤입니다. 이 해산물 국수는 꼭 한 번 경험해볼 가치가 있는 메뉴입니다!\n\n📌 영업시간:\n평일: 11:00 AM - 4:00 PM\n주말: 11:00 AM - 7:00 PM")]
                )
            )
        elif text == '八條壽司簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="這家日式料理店菜色選擇豐富多元，從新鮮的生魚片🍣、精緻的握壽司🍙，到各類炒物、炸物、烤物🍤應有盡有。平日中午更推出超值的商業午餐套餐，深受顧客喜愛。其中，八條壽司的壽司拼盤是店內的招牌必點，以當日最新鮮的食材精心製作，每次用餐都能享受到不一樣的美味體驗。無論是品質還是價格，這間店可以稱為是鶯歌地區最強的平價日本料理！\n\n📌營業資訊\n平日 11:30-13:30、17:00-20:30\n假日 11:00-13:40、16:30-21:00")]
                )
            )
        elif text == '八條壽司Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="This Japanese restaurant offers a diverse and abundant menu, ranging from fresh sashimi 🍣 and delicate nigiri 🍙 to a variety of stir-fried, fried, and grilled dishes 🍤. On weekdays, they also provide value-packed lunch sets, which are highly popular among customers. The sushi platter featuring eight pieces is a must-try signature dish, carefully prepared with the freshest ingredients of the day, ensuring a unique and delicious experience every time. Whether it’s for quality or affordability, this restaurant is undoubtedly the best value Japanese cuisine in the Yingge area!\n\n📌 Business Hours:\nWeekdays: 11:30 AM - 1:30 PM, 5:00 PM - 8:30 PM\nWeekends: 11:00 AM - 1:40 PM, 4:30 PM - 9:00 PM")]
                )
            )
        elif text == '八條壽司紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="この日本料理店は、豊富で多彩なメニューが自慢です。新鮮な刺身🍣、繊細な握り寿司🍙から、炒め物、揚げ物、焼き物🍤まで何でも揃っています。平日にはお得なランチセットも提供しており、多くの顧客に愛されています。特に、八貫の寿司盛り合わせは店の看板メニューで、その日の最も新鮮な食材を使って丁寧に作られるため、毎回異なる美味しさを楽しめます。品質も価格も優れており、鶯歌エリアで最強のコスパ日本料理店と言えるでしょう！\n\n📌 営業時間：\n平日：11:30 - 13:30、17:00 - 20:30\n週末：11:00 - 13:40、16:30 - 21:00")]
                )
            )
        elif text == '八條壽司소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="이 일본 음식점은 다양하고 풍부한 메뉴를 자랑합니다. 신선한 사시미 🍣, 정교한 니기리 초밥 🍙부터 볶음 요리, 튀김 요리, 구이 요리 🍤까지 모두 갖추고 있습니다. 평일에는 가성비 높은 점심 세트 메뉴도 제공하며, 많은 손님들에게 인기가 있습니다. 특히 여덟 가지 초밥으로 구성된 초밥 플래터는 이 가게의 대표 메뉴로, 매일 가장 신선한 재료로 정성껏 만들어져 매번 새로운 맛을 경험할 수 있습니다. 품질과 가격 모두 뛰어나 잉거 지역 최고의 가성비 일본 요리점이라고 할 수 있습니다!\n\n📌 영업시간:\n평일: 오전 11:30 - 오후 1:30, 오후 5:00 - 오후 8:30\n주말: 오전 11:00 - 오후 1:40, 오후 4:30 - 오후 9:00")]
                )
            )
        elif text == '勇伯垃圾麵簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「勇伯垃圾麵」是在地超過50年的老店，湯頭以豬骨精燉熬煮而成從不去渣，因湯頭看起來混濁，被稱為是「垃圾麵」🍜，而且是間很平價的銅板小吃店🪙，連在地人都很愛🤩，也有特地跑來吃的外地遊客。推薦下次來鶯歌玩的時候，可以來嘗嘗這碗獨特的「垃圾麵」喔🤤！\n\n📌營業資訊\n每日：16:00-23:00")]
                )
            )
        elif text == '勇伯垃圾麵Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'Yong Bo Garbage Noodles' is a local eatery with over 50 years of history. Its broth is meticulously simmered with pork bones, unfiltered, resulting in a cloudy appearance, which earned it the name 'Garbage Noodles' 🍜. Despite the name, it’s a delicious and affordable dish, beloved by locals 🪙 and even attracting tourists from afar 🤩. When you visit Yingge, don’t miss the chance to try this unique bowl of 'Garbage Noodles' 🤤!\n\n📌 Business Hours\nDaily: 4:00 PM - 11:00 PM")]
                )
            )
        elif text == '勇伯垃圾麵紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「勇伯ゴミ麺（ヨンボゴミメン）」は、50年以上の歴史を誇る地元の老舗店です。スープは豚骨をじっくり煮込んで作られ、濾されないため、濁った見た目が特徴で「ゴミ麺」と呼ばれています🍜。名前はユニークですが、その美味しさは折り紙付きで、価格も非常にお手頃🪙。地元の人々に愛されており🤩、遠方からわざわざ食べに来る観光客も多いです。次回鶯歌を訪れる際は、このユニークな「ゴミ麺」をぜひ試してみてください🤤！\n\n📌 営業時間\n毎日：16:00～23:00")]
                )
            )
        elif text == '勇伯垃圾麵소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「용보 쓰레기 면」은 50년 이상의 역사를 자랑하는 현지 노포입니다. 국물은 돼지뼈를 정성스럽게 끓여내며 걸러내지 않아 뿌연 외관을 가지고 있어 '쓰레기 면'이라는 독특한 이름이 붙었습니다🍜. 이름은 독특하지만 맛은 훌륭하며, 가격도 매우 저렴해🪙 현지인들에게 사랑받는 음식입니다🤩. 멀리서 일부러 찾아오는 관광객들도 많습니다. 다음에 잉거를 방문할 때 이 독특한 '쓰레기 면'을 꼭 맛보세요🤤!\n\n📌 영업시간\n매일: 오후 4:00 - 오후 11:00")]
                )
            )
        elif text == '厚道飲食店簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌老街超人氣古早味排骨飯專賣店「厚道飲食店」，店內裝潢彷彿穿越時光隧道，有著濃厚的懷舊氛圍。以懷舊風味的排骨飯為招牌🍱，排骨炸得很酥香入味，肉帶有厚度，鹹香好吃🤤，每一口都讓人回味無窮。來到鶯歌老街，不僅要漫遊古街，更別錯過這家「厚道飲食店」，讓您品味道地的經典台灣風味！\n\n📌營業資訊\n平日：11:00-14:30、16:30-19:00\n假日：11:00-17:00、16:30-19:00")]
                )
            )
        elif text == '厚道飲食店Introduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Popular Old-Fashioned Pork Chop Rice at 'Hou Dao Dining' on Yingge Old Street\nStep into 'Hou Dao Dining' and feel as if you’ve traveled back in time, with its nostalgic decor creating a warm, retro atmosphere. The signature pork chop rice 🍱 features perfectly crispy, flavorful pork chops with tender meat that’s both savory and delicious 🤤. Every bite will leave you wanting more. When visiting Yingge Old Street, don’t just stroll around—make sure to stop by 'Hou Dao Dining' and savor the authentic taste of traditional Taiwanese flavors!\n\n📌 Business Hours\nWeekdays: 11:00–14:30, 16:30–19:00\nWeekends: 11:00–17:00, 16:30–19:00")]
                )
            )
        elif text == '厚道飲食店紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌老街の人気古早味排骨飯専門店「厚道飲食店」\n「厚道飲食店」に足を踏み入れると、まるで時空を超えたような、懐かしさ溢れる店内に包まれます。看板メニューの排骨飯🍱は、外はサクサク、中はジューシーな豚排骨で、塩気の効いた美味しさが特徴です🤤。一口食べれば、思わずもっと食べたくなる味わい。鶯歌老街に訪れた際には、街歩きだけでなく、「厚道飲食店」で本格的な台湾の味を楽しんでください！\n\n📌 営業時間\n平日：11:00–14:30、16:30–19:00\n週末：11:00–17:00、16:30–19:00")]
                )
            )
        elif text == '厚道飲食店소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌老街 인기 고풍스러운 배추찜 전통식당 '후도 음식점'\n'후도 음식점'에 들어서면 마치 시간 여행을 떠난 듯한, 고풍스러운 인테리어로 가득한 따뜻한 분위기를 느낄 수 있습니다. 대표 메뉴인 배추찜 밥🍱은 겉은 바삭하고 속은 부드러운 돼지 갈비로, 짭짤하고 맛있습니다🤤. 한 입 먹으면 입에 남는 맛이 계속 생각납니다. 鶯歌老街에 오시면 거리 탐방뿐만 아니라 '후도 음식점'에서 전통 대만의 맛을 꼭 경험해 보세요!\n\n📌 영업 시간\n평일: 11:00–14:30, 16:30–19:00\n주말: 11:00–17:00, 16:30–19:00")]
                )
            )
        elif text == '公車':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「小小行動，大大改變，讓我們一起減碳！🚌🚄🚲👣」\n\n搭乘大眾運輸工具不僅是便利的出行方式，更是有效減碳的絕佳選擇🥇！當我們選擇搭乘大眾工具時，能夠大幅降低碳足跡，並改善空氣品質。🌡️\n\n為此我們選擇了兩條三峽與鶯歌通勤的公車路線，以供您們參考🥰\n-\n702🚌\nhttps://reurl.cc/kM8903\n-\n981🚌\nhttps://reurl.cc/6jbXaZ")]
                )
            )
        elif text == 'Bus':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'Small actions, big changes—let's reduce carbon emissions together! 🚌🚄🚲👣'\n\nUsing public transportation is not only a convenient way to travel but also an excellent choice for reducing carbon emissions 🥇! By choosing public transit, we can significantly lower our carbon footprint and improve air quality. 🌡️\n\nTo support this, we’ve selected two bus routes connecting Sanxia and Yingge for your reference. 🥰\n-\n702🚌\nhttps://reurl.cc/kM8903\n-\n981🚌\nhttps://reurl.cc/6jbXaZ")]
                )
            )
        elif text == '버스':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'작은 행동이 큰 변화를 만듭니다—함께 탄소를 줄여요! 🚌🚄🚲👣'\n\n대중교통을 이용하는 것은 편리한 이동 수단일 뿐만 아니라 탄소 배출을 줄이는 데 탁월한 선택입니다 🥇! 대중교통을 선택함으로써 탄소 발자국을 크게 줄이고 공기 질을 개선할 수 있습니다. 🌡️\n\n이를 위해 삼협(산샤)과 응가(잉거)를 연결하는 통근 버스 노선 두 개를 추천드립니다. 🥰\n-\n702🚌\nhttps://reurl.cc/kM8903\n-\n981🚌\nhttps://reurl.cc/6jbXaZ")]
                )
            )
        elif text == 'バス':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「小さな行動が大きな変化を生む！一緒に炭素削減に取り組みましょう！🚌🚄🚲👣」\n\n公共交通機関を利用することは、便利な移動手段であるだけでなく、炭素削減のための素晴らしい選択肢でもあります🥇！公共交通を選ぶことで、炭素足跡を大幅に削減し、空気の質を改善することができます。🌡️\n\nそのため、三峽（サンシャ）と鶯歌（イングー）を結ぶ通勤用バス路線を2つご紹介しますので、ぜひ参考にしてください。🥰\n-\n702🚌\nhttps://reurl.cc/kM8903\n-\n981🚌\nhttps://reurl.cc/6jbXaZ")]
                )
            )
        elif text == '捷運':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「讓每一次搭乘都成為為地球盡一份心力的機會！🫡」\n\n搭捷運就像給地球穿上了一雙「減碳鞋👟」！每當你踏進捷運車廂，不僅能享受快速穿梭的快感，還能幫助地球減少一點碳排放🤩。\n\n每一站的停止都是對減碳的一次小小承諾，讓我們的地球🌍呼吸更順暢。\n\n三鶯捷運預計將於2025年底完工❗️這未來將大幅減少通勤時間，讓從三鶯地區前往台北市的時間縮短約20分。")]
                )
            )
        elif text == 'MRT':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'Every ride is an opportunity to do your part for the planet! 🫡'\n\nTaking the MRT is like putting 'carbon-reducing shoes 👟' on the Earth! Every time you step into an MRT car, you're not just enjoying the convenience of fast travel but also helping reduce carbon emissions 🤩.\n\nEach station stop represents a small promise toward reducing emissions, letting our planet 🌍 breathe a little easier.\n\nThe San-Ying MRT is scheduled to be completed by the end of 2025❗️ This new line will significantly cut commuting times, reducing travel from the San-Ying area to Taipei City by approximately 20 minute.")]
                )
            )
        elif text == '지하철':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'탑승할 때마다 지구를 위한 마음을 담은 기회를 만들어 보세요! '\n\n지하철을 타는 것은 지구에' 탄소 감소 신발👟'을 신겨주는 것과 같습니다! 지하철 객실에 들어설 때마다 빠르고 편리한 이동을 즐길 뿐 아니라, 지구의 탄소 배출 감소에도 기여하게 됩니다🤩.\n\n각 정거장의 정차는 탄소 절감에 대한 작은 약속을 의미하며, 우리의 지구 🌍가 더 편히 숨 쉴 수 있게 도와줍니다.\n\n산잉(MRT) 노선은 2025년 말에 완공될 예정입니다❗️ 이 노선은 산잉 지역에서 타이베이 시까지의 통근 시간을 약 20분 단축할 것으로 기대됩니다🫵🏻.")]
                )
            )
        elif text == '地下鉄':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「乗るたびに地球のために心を込めた一歩を！🫡」\n\nMRTに乗ることは、地球に「カーボン削減シューズ👟」を履かせるようなものです！ MRT車両に足を踏み入れるたびに、スピーディーな移動を楽しむだけでなく、地球のCO2排出削減にも貢献できます🤩。\n\n各駅の停車は、カーボン削減に向けた小さな約束です🌍。私たちの地球がもっと楽に息をできるようにしましょう。\n\n三鶯MRTラインは2025年末に完成予定❗️これにより、三鶯地区から台北市への通勤時間が約20分短縮される見込みで。")]
                )
            )
        elif text == '自行車':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「與風共舞的踏板小英雄🚴🥇」\n\n自行車就像我們的綠色夥伴🫶🏻，帶著我們穿越城市的繁華與自然的寧靜。每一次的騎行，都是在減少碳排放，讓清新的空氣重新進入我們的生活中。🥳\n\n讓我們一起騎出一條清新、無污染的綠色之路，為地球🌍創造一個更美好的環境🌱！\n\n🔗為YouBike官方App，可直接查詢附近站點～🚲\nhttps://reurl.cc/EgbYVn\n-\n🔗為YouBike網頁版，需自行打地址查詢站點～🚲\nhttps://reurl.cc/74bYE1")]
                )
            )
        elif text == 'Bicycle':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="‘Little Heroes on Pedals Dancing with the Wind 🚴🥇’\n\nBicycles are like our green partners 🫶🏻, taking us through the bustling cityscapes and serene nature. Every ride reduces carbon emissions, bringing fresh air back into our lives 🥳.\n\nLet’s ride together to pave a clean, pollution-free green path and create a better environment 🌍 for our planet 🌱!\n🔗 https://reurl.cc/EgbYVn — Check nearby stations directly! 🚲\n\n🔗https://reurl.cc/74bYE1 — Search stations by address. 🚲")]
                )
            )
        elif text == '자전거':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="‘바람과 함께 춤추는 작은 영웅🚴🥇’\n\n자전거는 우리의 녹색 파트너🫶🏻로, 도시의 번잡함과 자연의 고요함을 넘나들게 합니다. 매번 페달을 밟을 때마다 탄소 배출을 줄이고, 신선한 공기를 우리의 삶으로 되돌립니다 🥳.\n\n함께 깨끗하고 오염 없는 녹색 길을 달리며, 지구🌍를 위한 더 나은 환경🌱을 만들어 봅시다!\n🔗https://reurl.cc/EgbYVn — 근처의 대여소를 바로 확인하세요! 🚲\n\n🔗https://reurl.cc/74bYE1— 주소를 입력하여 대여소를 검색하세요. 🚲")]
                )
            )
        elif text == '自転車':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「風と共に踊る小さなヒーロー🚴🥇」\n\n自転車は私たちのグリーンパートナー🫶🏻のような存在です。街の喧騒や自然の静けさを通り抜けるたびに、CO2排出量を減らし、新鮮な空気を生活に取り戻します🥳。\n\n一緒にクリーンで汚染のない緑の道を切り開き、地球🌍にもっと良い環境🌱を作りましょう！\n\n🔗https://reurl.cc/EgbYVn — 近くのステーションを直接チェックできます！ 🚲\n\n🔗 https://reurl.cc/74bYE1 — 住所を入力してステーションを検索してください。 🚲")]
                )
            )
        elif text == '三峽綠茶季簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="綠茶季：春天來了，茶香四溢！🌸\n\n活動日期：114/03/15-16\n地點：臺北大學心湖畔綠地\n\n今年的「吼你有春」綠茶季，邀請大家來感受茶鄉春意盎然的氛圍。\n活動亮點包括：\n1.綠茶創意市集：品嚐限定綠茶與創意茶點，探索三峽茶產業。\n2.文化探索區：藍染、茶器製作及茶鄉文化分享，帶你走進茶文化的故事。\n3.青年創意區：體驗茶葉與科技結合，挑戰DIY茶飲設計比賽。\n4.親子遊戲區：親子闖關，共享家庭時光。\n5.草地野餐派對：與親朋好友在綠地共度美好午後。\n6.春日表演饗宴：精彩表演，春日活力十足。\n7.茶味美食區：以綠茶為主題的美食，帶來味蕾驚喜！\n\n快來品味春天的茶香，與家人朋友一同享受這場茶鄉盛會！\n\n相關資訊：https://reurl.cc/M6MW3X")]
                )
            )
        
        elif text == 'SanxiaGreenTeaFestivalIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Spring Tea Festival in Sanxia: The Spring Is Here, with Fragrant Tea! 🌸\n\nEvent Dates: March 15 (Sat) - 16 (Sun), 2024\nLocation: Taipei University, Xinhu Lake Green Area\n\nThis year’s 'Spring Tea Festival' invites everyone to immerse themselves in the vibrant spring atmosphere of Sanxia, the tea hometown.\n\nHighlights of the event include:\n1.Green Tea Creative Market: Taste limited edition green teas and creative tea treats, and explore Sanxia's tea industry.\n2.Cultural Exploration Area: Experience indigo dyeing, tea ware making, and cultural stories of tea.\n3.Youth Creativity Zone: Experience the fusion of tea and technology, and challenge the DIY tea drink design competition.\n4.Family Fun Zone: Enjoy interactive games for parents and kids to share family time.\n5.Picnic Party on the Grass: Spend a lovely afternoon with friends and family on the green field.\n6.Spring Performance Feast: Enjoy vibrant performances full of spring energy.\n7.Tea-flavored Food Area: Savor special green tea-themed foods for a delightful culinary experience!\n\nCome and taste the spring tea aroma, and enjoy this tea-hometown festival with your loved ones!\n\nRelated Information: https://reurl.cc/M6MW3X")]
                )
            )
        elif text == '삼샤녹차축제소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="삼협 녹차 축제: 봄이 왔다, 차 향기가 퍼진다! 🌸\n\n행사 날짜: 2024년 3월 15일 (토) ~ 16일 (일)\n장소: 타이페이 대학교 신호호수 녹지\n\n올해 '봄차 축제'는 삼협의 봄의 기운을 만끽하며 여러분을 초대합니다. \n행사 하이라이트는 다음과 같습니다:\n1.녹차 창의 시장: 한정판 녹차와 창의적인 차 간식을 맛보고, 삼협의 차 산업을 탐험해 보세요.\n2.문화 탐방 구역: 블루 염색, 차기 제작, 차 문화 이야기를 통해 차의 역사와 문화를 깊이 있게 알아보세요.\n3.청년 창의 구역: 차와 기술의 융합을 체험하고, DIY 차 음료 디자인 대회에 도전해 보세요.\n4.가족 게임 구역: 가족과 함께 즐기는 다양한 퀴즈와 놀이, 즐거운 시간을 보내세요.\n5.초원 피크닉 파티: 친구들과 가족과 함께 초원에서 여유로운 오후를 즐기세요.\n6.봄날 공연 향연: 봄의 활력을 느낄 수 있는 멋진 공연들이 펼쳐집니다.\n7.차 맛 음식 구역: 녹차를 테마로 한 음식들이 한자리에 모여 입맛을 사로잡습니다!\n\n봄의 차 향기를 느끼며, 가족 및 친구들과 함께 이 차의 고향 축제를 즐겨보세요!\n\n관련 정보： https://reurl.cc/M6MW3X")]
                )
            )
        elif text == '三峡緑茶祭り紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="春の三峡緑茶祭り: 春が来た、茶の香りが広がる！🌸\n\nイベント日程：2024年3月15日（土）〜16日（日）\n場所：台北大学心湖畔緑地\n\n今年の「春茶祭り」は、三峡の春の息吹を感じながら、皆さんに楽しんでいただけるイベントです。\nイベントのハイライトは以下の通りです：\n1.緑茶クリエイティブマーケット：限定緑茶や創作茶点を試飲し、三峡の茶産業を探求します。\n2.文化探求エリア：藍染、茶器作り、茶の文化を深く知るためのシェアリング。\n3.若者クリエイティブエリア：茶とテクノロジーの融合を体験し、DIY茶飲み設計コンテストに挑戦！\n4.親子ゲームエリア：親子で協力し、楽しみながら時間を過ごします。\n5.草地ピクニックパーティ：友人や家族とともに、緑地で素敵な午後のひとときを楽しんでください。\n6.春のパフォーマンスフェスタ：春のエネルギーに満ちた素晴らしいパフォーマンスをお楽しみください。\n7.緑茶フードエリア：緑茶をテーマにした食べ物をお楽しみください、味覚の旅が広がります！\n\n春の茶香を楽しみながら、大切な人たちとこの茶の街の祭りを満喫しましょう！\n\n関連情報： https://reurl.cc/M6MW3X")]
                )
            )
        elif text == '祖師廟賽豬公簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="時間 : 農曆正月初六 2025/02/03\n地點 : 三峽祖師廟前廣場 \n\n清水祖師生日，每年農曆正月初六是清水祖師誕辰。\n三峽長福巖祖師廟，供奉的是來自福建省泉州安溪縣的清水祖師。每年農曆正月初六也就是清水祖師聖誕日，三峽祖師廟都會舉行盛大的神豬祭典比賽。飼主們將神豬抬上華麗的燈台，簪花掛紅，豬毛修剪成花邊圖樣，並在口裡塞鳳、刁桔，表達對清水祖師爺的敬意。中午祭祀結束後，神豬將宰切分送給信眾，並開放民眾拔神豬毛，相傳可有平安之福。🧧\n\n相關資訊 https://reurl.cc/EgbDq0")]
                )
            )
        elif text == 'SacredPigCompetitionIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Time: Lunar New Year 6th, 2025/02/03\nLocation: Front Plaza of Sanxia Zushi Temple\n\nEvery year on the 6th day of the Lunar New Year, Sanxia Changfu Rock Zushi Temple celebrates the birthday of Qing Shui Zushi with a grand Divine Pig competition. Qing Shui Zushi is a revered deity from Anxi County, Quanzhou, Fujian Province. On this day, pig owners display their divine pigs on elaborately decorated platforms, trimming their fur into beautiful patterns and placing pineapples and tangerines in their mouths to show respect to Qing Shui Zushi. After the noon ceremony, the pigs are butchered and shared with the public, and attendees can pluck the divine pig's fur, which is believed to bring peace and blessings.🧧\n\nRelated Information: https://reurl.cc/EgbDq0")]
                )
            )
        elif text == '돼지공양대회소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="시간: 음력 정월 초육일, 2025년 2월 3일\n장소: 삼협 조사사 앞 광장\n\n매년 음력 정월 초육일은 청수조사의 생일이며, 삼협 장복암 조사사에서는 신성한 돼지 제전 대회를 개최하여 이 날을 기념합니다. 삼협 조사사에는 푸젠성 천저우 안시현에서 온 청수조사가 모셔져 있습니다. 이날, 돼지 주인들은 신성한 돼지를 화려한 등대에 올리고 돼지의 털을 아름다운 꽃무늬로 다듬고, 입에 파인애플과 귤을 넣어 청수조사에 대한 존경을 표합니다. 제사가 끝난 후, 신성한 돼지는 도축되어 신도들에게 나누어지며, 참가자들은 돼지의 털을 뽑을 수 있는데, 이는 평안과 축복을 가져다준다고 전해집니다.🧧\n\n관련 정보：https://reurl.cc/EgbDq0")]
                )
            )
        elif text == '豚奉納祭紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="時間: 旧正月6日 2025/02/03\n場所: 三峡祖師廟前広場\n\n毎年、旧正月の6日は清水祖師の誕生日であり、三峡長福巖祖師廟では盛大な神豬祭りが行われます。三峡祖師廟には、福建省泉州安溪県から来た清水祖師が祀られています。この日は、飼い主たちが神豬を華やかな燈台に載せ、豚毛を花の形に整え、口にパイナップルやミカンを詰めて清水祖師に敬意を表します。祭りが終わると、神豬は切り分けられ、信者に分け与えられ、参加者は神豬の毛を引き抜くことができるとされ、これは平安と祝福をもたらすと信じられています。🧧\n\n関連情報：https://reurl.cc/EgbDq0")]
                )
            )
        elif text == '三峽藍染節簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="時間 : 每年7-8月\n地點 : 三峽染工坊、三峽老街\n\n自2002年起，新北市三峽區公所每年於七、八月舉辦藍染節，致力於傳承與推廣藍染工藝文化。活動內容包括藍染特展、體驗、表演及小旅行，吸引民眾深入了解藍染的魅力。三峽曾是藍染的發源地👣，得天獨厚的水質與地理條件促成了當地染布業的繁榮。隨著藍染技藝的重生，透過現代的復古時尚，藍染不僅喚起了在地記憶，也吸引外地遊客來體驗這項珍貴的文化遺產。藍染節因此成為一項推動文化傳承的重要活動️‼️\n\n相關資訊：https://www.sanxias.com.tw/portal_b1_page.php?owner_num=b1_57622&button_num=b1&cnt_id=13578")]
                )
            )
        elif text == 'SanxiaIndigoDyeingFestivalIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Time: Every July and August\nLocation: Sanxia Dye Workshops, Sanxia Old Street\n\nSince 2002, the Sanxia District Office of New Taipei City has held the Indigo Dyeing Festival every July and August, dedicated to preserving and promoting the craft of indigo dyeing. The event includes indigo exhibitions, hands-on experiences, performances, and mini tours, drawing people to explore the charm of indigo dyeing. Sanxia was once the birthplace of indigo dyeing 👣, with its exceptional water quality and geographical conditions fostering the prosperity of the local dyeing industry. With the revival of indigo dyeing techniques, the craft has been reintroduced through modern retro fashion, evoking local memories and attracting visitors to experience this precious cultural heritage. The Indigo Dyeing Festival has thus become an important event for promoting cultural heritage‼️\n\nRelated Information: https://www.sanxias.com.tw/portal_b1_page.php?owner_num=b1_57622&button_num=b1&cnt_id=13578")]
                )
            )
        elif text == '삼샤쪽염색축제소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="시간: 매년 7월과 8월\n장소: 삼협 염색 공방, 삼협 올드 스트리트\n\n2002년부터 신북시 삼협구는 매년 7월과 8월에 인디고 염색 축제를 개최하여 인디고 염색 공예 문화를 전수하고 홍보하는 데 힘쓰고 있습니다. 이 행사에서는 인디고 염색 특별 전시, 체험, 공연 및 소규모 여행이 포함되어 사람들을 유인하여 인디고 염색의 매력을 탐구하게 만듭니다. 삼협은 한때 인디고 염색의 발상지👣였으며, 뛰어난 수질과 지리적 조건이 지역 염색 산업의 번영을 이끌었습니다. 인디고 염색 기술의 부활로, 현대의 복고풍 패션을 통해 염색은 지역의 기억을 되살리고 외부에서 방문하는 관광객들을 이 귀중한 문화유산을 체험하게 합니다. 인디고 염색 축제는 문화 유산을 전파하는 중요한 행사로 자리잡고 있습니다‼️\n\n관련 정보：https://www.sanxias.com.tw/portal_b1_page.php?owner_num=b1_57622&button_num=b1&cnt_id=13578")]
                )
            )
        elif text == '三峡藍染祭り紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="時間: 毎年7月〜8月\n場所: 三峡染工房、三峡老街\n\n2002年から、新北市三峡区は毎年7月と8月に「藍染フェスティバル」を開催しており、藍染工芸の伝承と普及に力を入れています。イベント内容には藍染特別展示、体験、パフォーマンス、小旅行などがあり、参加者は藍染の魅力を深く学ぶことができます。三峡はかつて藍染の発祥地👣であり、優れた水質と地理的条件が地元の染物業の繁栄を支えてきました。藍染技術の復活により、現代のレトロファッションを通じて、藍染は地域の記憶を呼び起こし、外部の観光客を引き寄せる貴重な文化遺産として体験されています。この藍染フェスティバルは、文化遺産を推進する重要なイベントとなっています‼️\n\n関連情報：https://www.sanxias.com.tw/portal_b1_page.php?owner_num=b1_57622&button_num=b1&cnt_id=13578")]
                )
            )
        elif text == '三峽老街龍舟創意賽簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="時間 : 每年端午節假期 2025/05/30-31\n地點 : 三峽老街\n\n「三峽河」辦理龍舟賽已經有百年的歷史，今三峽河已無法再舉辦龍舟賽🚣，於是新北市政府將龍舟賽搬至三峽老街上，希望將三峽賽龍舟「曾經的榮耀」🏆、「傳統文化」與「常民記憶」結合目前的國際趨勢🌍「節能環保」♻️，復刻並創造「三峽獨有的端午節龍舟競技」，讓老一輩可以緬懷過去，讓年輕一輩可以創新傳承。「三峽老街」於6月8日辦理全新北首創「三峽新船說 老街創意龍舟賽」。\n\n相關資訊：https://reurl.cc/vpKGRo")]
                )
            )
        
        elif text == 'CreativeDragonBoatRaceIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Time: Every year during the Dragon Boat Festival holiday (May 30-31, 2025)\nLocation: Sanxia Old Street\n\nThe Dragon Boat Race on the 'Sanxia River'' has a history of over a century. However, the river is no longer suitable for hosting the event🚣. To preserve this tradition, the New Taipei City Government has relocated the race to Sanxia Old Street. This initiative integrates the 'former glory'🏆, 'traditional culture,' and 'local memories' of Sanxia's Dragon Boat Race with the global trends🌍 of 'energy conservation and environmental protection'♻️. The goal is to recreate and innovate a 'Sanxia-exclusive Dragon Boat Competition' for the Dragon Boat Festival, allowing the older generation to reminisce and the younger generation to creatively inherit this tradition.\nOn June 8, 'Sanxia Old Street' will host New Taipei's first-ever 'Sanxia New Boat Story: Creative Dragon Boat Race on Old Street.'\n\nRelated Information: https://reurl.cc/vpKGRo")]
                )
            )
        elif text == '창의적인용선대회':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="시간: 매년 단오절 연휴 (2025년 5월 30일~31일)\n장소: 싼샤 올드 스트리트\n\n'싼샤 강'에서 열리는 용선 경기는 100년 이상의 역사를 자랑하는 전통 행사입니다. 그러나 현재 강에서는 더 이상 경기를 개최할 수 없게 되었고🚣, 신베이시 정부는 이 전통을 이어가기 위해 경기를 싼샤 올드 스트리트로 옮겼습니다. 이 행사는 싼샤 용선 경주의 '과거의 영광'🏆, '전통 문화', '지역 주민의 기억'과 함께 현대적인 '에너지 절약 및 환경 보호'♻️라는 국제적 트렌드🌍를 결합한 새로운 형태로 탄생했습니다. 이를 통해 '싼샤만의 독특한 단오절 용선 경기'를 재현하고, 어르신들에게는 과거를 회상할 기회를, 젊은 세대에게는 혁신적으로 계승할 기회를 제공합니다.\n6월 8일, 신베이 최초의 '싼샤 뉴 보트 스토리: 창의적인 올드 스트리트 용선 경기'가 싼샤 올드 스트리트에서 열립니다.\n\n관련 정보：https://reurl.cc/vpKGRo")]
                )
            )
        elif text == '創意ドラゴンボート大会紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="日時: 毎年端午節の連休 (2025年5月30日～31日)\n場所: 三峡老街\n\n「三峡河」でのドラゴンボートレースは百年以上の歴史を持つ伝統行事です。しかし、現在の三峡河ではレースを開催することができなくなりました🚣。そこで、新北市政府はこのレースを三峡老街に移し、三峡のドラゴンボートレースの「かつての栄光」🏆、「伝統文化」、「地域の記憶」を、現代の「省エネ・環境保護」♻️という国際的なトレンド🌍と融合させました。このイベントは「三峡独自の端午節ドラゴンボート競技」を復刻し、年配者には過去を懐かしんでもらい、若い世代には創造的に伝承してもらうことを目指しています。\n6月8日、新北市初となる「三峡新船物語 老街創意ドラゴンボートレース」が「三峡老街」で開催されます。\n\n関連情報：https://reurl.cc/vpKGRo")]
                )
            )
        elif text == '鶯歌產地開放日簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌陶瓷繼承者們聯手打造🤝「鶯歌產地開放日」，以「展現鶯歌陶瓷產地如何運作」為概念💡，打造「引發新鮮事」的綜合體驗空間。帶領觀者了解鶯歌陶瓷產地的技術強項所在，將鶯歌老街與工廠串連成一個綜合體驗型空間，引導大眾在過程中逐一了解鶯歌陶瓷產地的運作邏輯，以及時至今日依舊毫不遜色的技術與美學。\n\n相關資訊：https://www.yinggeopenhouse.com/origin")]
                )
            )
        elif text == 'YinggeOpenFactoryDayIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="The inheritors of Yingge ceramics have joined forces🤝 to present the 'Yingge Origin Open Day.' With the concept of 'showcasing how the Yingge ceramic origin operates'💡, this event creates a comprehensive experiential space full of fresh discoveries. Visitors are guided to explore the technical strengths of Yingge’s ceramic production, connecting Yingge Old Street and factories into an integrated experience. This journey allows the public to understand the operational logic behind Yingge ceramics and appreciate the enduring excellence in its technology and aesthetics.\n\nRelated Information:https://www.yinggeopenhouse.com/origin")]
                )
            )
        elif text == '잉거생산지개방의날대회':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="잉거 도자기의 계승자들이 손을 맞잡고🤝 '잉거 원산지 오픈 데이'를 개최합니다. '잉거 도자기 생산지가 어떻게 운영되는지 보여준다'는 💡개념으로, '새로운 발견을 촉진하는' 종합 체험 공간을 만들어냅니다. 관람객들은 잉거 도자기 생산지의 기술적 강점을 탐구하고, 잉거 올드 스트리트와 공장을 하나로 연결한 통합 경험 공간을 통해 여정을 떠나게 됩니다. 이 과정을 통해 잉거 도자기 생산지의 운영 논리를 하나씩 이해하고, 오늘날에도 뒤떨어지지 않는 기술과 미학을 만끽할 수 있습니다.\n\n관련 정보：https://www.yinggeopenhouse.com/origin ")]
                )
            )
        elif text == '鶯歌産地開放デー紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌（イングー）の陶磁器の継承者たちが手を取り合い🤝、「鶯歌産地オープンデー」を開催します。「鶯歌陶磁器の産地がどのように運営されているかを紹介する」💡をコンセプトに、「新しい発見を引き起こす」総合体験空間を提供します。観覧者を陶磁器産地の技術の強みを探る旅へと誘い、鶯歌老街と工場を一つの統合型体験空間としてつなげます。このプロセスを通じて、鶯歌陶磁器産地の運営論理を順に理解し、今日でも劣らない技術と美学を堪能することができます。\n\n関連情報：https://www.yinggeopenhouse.com/origin")]
                )
            )
        elif text == '鶯歌嘉年華簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌嘉年華致力於振興地方經濟並推廣陶瓷文化🫖。活動由新北市政府策劃，邀請遊客深入探索工廠與鶯歌老街，全面了解陶瓷產業悠久的歷史與新時代的創新轉型✨。透過一系列豐富多元的活動，參加者不僅可以欣賞精美的陶瓷工藝，還能親身體驗製作過程，深刻感受手作工藝的獨特魅力。這場盛會將進一步提升鶯歌在地品牌的知名度與影響力🔝！\n\n相關資訊：https://newtaipei.travel/zh-tw/calendar/detail/2685")]
                )
            )
        elif text == 'YinggeCarnivalIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Yingge Carnival is committed to revitalizing the local economy and promoting ceramic culture🫖. Organized by the New Taipei City Government, the event invites visitors to explore factories and Yingge Old Street, offering an in-depth look at the long history of the ceramics industry and its modern innovations✨. Through a diverse range of activities, participants can not only admire exquisite ceramic craftsmanship but also experience the making process firsthand, immersing themselves in the charm of handmade art. This grand event aims to elevate the recognition and influence of Yingge’s local brand🔝.\n\nRelated Information:https://newtaipei.travel/zh-tw/calendar/detail/2685")]
                )
            )
        elif text == '잉거카니발':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="잉거 카니발은 지역 경제를 활성화하고 도자기 문화를 홍보하는 데 전념하고 있습니다🫖. 신베이시 정부가 주최하는 이 행사는 방문객들이 공장과 잉거 올드 스트리트를 탐방하며, 도자기 산업의 오랜 역사와 현대적 혁신을 깊이 이해할 수 있도록 돕습니다✨. 다양한 활동을 통해 참가자들은 정교한 도자기 공예를 감상할 뿐만 아니라 직접 제작 과정을 체험하며 핸드메이드 예술의 독특한 매력을 느낄 수 있습니다. 이 축제는 잉거 지역 브랜드의 인지도와 영향력을 한층 더 높이는 것을 목표로 하고 있습니다🔝.\n\n관련 정보：https://newtaipei.travel/zh-tw/calendar/detail/2685")]
                )
            )
        elif text == '鶯歌カーニバル紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="鶯歌カーニバルは、地域経済の活性化と陶磁器文化の推進に力を注いでいます🫖。新北市政府の主催により、訪問者は工場や鶯歌老街を探索し、陶磁器産業の長い歴史と現代における革新を深く知ることができます✨。多彩な活動を通じて、参加者は美しい陶磁器工芸品を鑑賞するだけでなく、製作体験を通じて手作りの魅力を味わうことができます。この祭典は、鶯歌の地域ブランドの知名度と影響力をさらに向上させることを目指しています🔝\n\n関連情報：https://newtaipei.travel/zh-tw/calendar/detail/2685")]
                )
            )
        elif text == '茶鄉故事簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「小小繪本，大大故事，一起傳承三峽綠茶文化！📖🍵🌱」\n\n三峽綠茶，不僅是臺灣的一抹青翠，更是三峽人文、自然與傳統技藝的象徵。\n為了讓更多人了解這片茶葉背後的故事，我們創作了一本結合教育與藝術的繪本，以動人的情節與精美的插畫，將三峽綠茶文化呈現在每位讀者眼前💚。\n\n茶香書香共飄揚，讓我們一起傳承三峽綠茶的美好！🌿🍵📖")]
                )
            )
        elif text == 'TeaVillageStoryIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="A Little Picture Book, A Big Story: Let’s Preserve the Culture of Sanxia Green Tea! 📖🍵🌱\n\nSanxia green tea is not just a verdant treasure of Taiwan but also a symbol of Sanxia’s humanity, nature, and traditional craftsmanship.\nTo help more people understand the story behind these tea leaves, we have created a picture book that combines education and art, presenting the culture of Sanxia green tea through captivating narratives and exquisite illustrations. 💚\n\nLet the aroma of tea and the charm of books spread far and wide. Together, let’s pass on the beauty of Sanxia green tea! 🌿🍵📖")]
                )
            )
        elif text == '茶の里の物語紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="小さな絵本、大きな物語。三峡緑茶文化を伝えよう！📖🍵🌱\n\n三峡緑茶は、台湾の緑の象徴であるだけでなく、三峡の人文、自然、そして伝統技術の象徴でもあります。\nこの茶葉に秘められた物語をより多くの人々に伝えるために、教育と芸術を融合させた絵本を制作しました。感動的なストーリーと美しいイラストを通じて、三峡緑茶文化を読者の皆さまにお届けします。💚\n\nお茶の香りと本の魅力を広め、一緒に三峡緑茶の美しさを伝えていきましょう！🌿🍵📖")]
                )
            )
        elif text == '차마을이야기소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="작은 그림책, 큰 이야기: 산샤 녹차 문화를 전승합시다! 📖🍵🌱\n\n산샤 녹차는 대만의 초록빛 보물일 뿐만 아니라, 산샤의 인문, 자연, 전통 기술을 상징합니다.\n이 차잎에 담긴 이야기를 더 많은 사람들에게 알리기 위해, 교육과 예술을 결합한 그림책을 제작하였습니다. 감동적인 이야기와 정교한 삽화를 통해 산샤 녹차 문화를 독자들에게 전합니다. 💚\n\n차 향기와 책의 매력을 함께 나누며, 산샤 녹차의 아름다움을 우리 함께 전승합시다! 🌿🍵📖")]
                )
            )
        elif text == '陶藝物語簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="小小繪本，大大世界，一起探索陶瓷文化的美好！📖🏺✨\n\n陶瓷，是泥土與火焰的對話，更是歷史與藝術的結晶。從實用的器具到藝術的創作，陶瓷承載了豐富的人文故事與生活美學。為了讓更多人了解陶瓷文化的魅力，我們創作了一本精緻的繪本，以生動的故事和精美的插圖，帶領讀者踏上一場陶瓷文化的探索之旅💚。\n\n陶香書香共譜章，讓我們透過一本繪本，連結泥土與藝術，探索陶瓷文化的無限可能！📖🏺✨")]
                )
            )
        elif text == 'CeramicArtTaleIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="A Little Picture Book, A Big World: Let’s Discover the Beauty of Ceramic Culture! 📖🏺✨\n\nCeramics are a dialogue between clay and fire, and a fusion of history and art.\nFrom practical tools to artistic creations, ceramics carry rich stories of humanity and the aesthetics of daily life. To help more people appreciate the charm of ceramic culture, we have created a beautifully illustrated picture book. Through engaging stories and exquisite illustrations, it invites readers to embark on a journey of ceramic exploration. 💚\n\nLet the aroma of ceramics and books weave together a beautiful chapter. Through this picture book, let’s connect clay with art and uncover the infinite possibilities of ceramic culture! 📖🏺✨")]
                )
            )
        elif text == '陶芸の物語紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="小さな絵本、大きな世界。一緒に陶磁文化の美しさを探求しましょう！📖🏺✨\n\n陶磁器は、粘土と炎の対話であり、歴史と芸術の結晶でもあります。実用品から芸術作品に至るまで、陶磁器は豊かな人間の物語と生活美学を内包しています。この陶磁文化の魅力を多くの人々に伝えるため、私たちは精巧な絵本を制作しました。生き生きとした物語と美しいイラストを通じて、読者を陶磁文化の探求の旅へと誘います。💚\n\n陶の香りと本の香りが一緒に織りなす章を、絵本を通して粘土と芸術をつなげ、陶磁文化の無限の可能性を探りましょう！📖🏺✨")]
                )
            )
        elif text == '도예이야기소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="작은 그림책, 큰 세상: 함께 도자기 문화의 아름다움을 탐구해요! 📖🏺✨\n\n도자기는 흙과 불의 대화이자, 역사와 예술의 결정체입니다. 실용적인 도구에서부터 예술적 창작물까지, 도자기는 풍부한 인간 이야기와 생활 미학을 담고 있습니다. 도자기 문화의 매력을 더 많은 사람들에게 전하기 위해, 우리는 정교한 그림책을 제작했습니다. 생생한 이야기와 아름다운 삽화를 통해 독자를 도자기 문화 탐험의 여정으로 안내합니다. 💚\n\n도자의 향기와 책의 향기가 함께 어우러지는 장을, 이 그림책을 통해 흙과 예술을 연결하고 도자기 문화의 무한한 가능성을 탐구해봅시다! 📖🏺✨")]
                )
            )
        elif text == '染出美好簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="小小繪本，大大色彩，一起探索藍染文化的美好！📖💙✨\n\n藍染，是自然與匠心的結合，更是傳統工藝與生活藝術的展現。從一片植物葉開始，經過發酵、浸染與晾曬，成就出那抹溫暖且深邃的藍色。藍染不僅是技術的傳承，更融入了人們的生活，象徵著自然的韻律與文化的深度。\n為了讓更多人了解這項珍貴的工藝，我們創作了一本結合教育與藝術的繪本，帶領讀者透過故事與插畫，感受藍染文化的魅力💚。\n\n藍香書香共飄揚，讓我們透過一本繪本，走進自然與工藝的交織，探索藍染文化的無限可能！📖💙✨")]
                )
            )
        elif text == 'DyeingBeautyIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="A Little Picture Book, A Big Palette: Let’s Discover the Beauty of Indigo Dyeing Culture! 📖💙✨\n\nIndigo dyeing is a fusion of nature and craftsmanship, and a reflection of traditional techniques and living art. Starting from a single leaf, through fermentation, dipping, and drying, it transforms into a warm and profound shade of blue. Indigo dyeing is not only a heritage of techniques but also a part of daily life, symbolizing the rhythm of nature and cultural depth.\n\nTo help more people understand this precious craft, we have created a picture book combining education and art. Through engaging stories and captivating illustrations, readers can experience the charm of indigo dyeing culture. 💚\n\nLet the aroma of indigo and books spread far and wide. Through this picture book, step into the intertwining of nature and craft, and explore the endless possibilities of indigo dyeing culture! 📖💙✨")]
                )
            )
        elif text == '美しさを染める紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="小さな絵本、大きな色彩。一緒に藍染文化の美しさを探求しましょう！📖💙✨\n\n藍染は自然と匠の技の融合であり、伝統工芸と生活芸術の象徴でもあります。一枚の植物の葉から始まり、発酵、浸染、乾燥を経て、温かく深い青色が生まれます。藍染は技術の継承だけでなく、人々の生活に溶け込み、自然のリズムと文化の深みを象徴しています。\nこの貴重な工芸をより多くの人々に知っていただくために、私たちは教育と芸術を融合させた絵本を制作しました。物語とイラストを通じて、読者の皆さまが藍染文化の魅力を感じられるようご案内します。💚\n\n藍の香りと本の香りが広がり、この絵本を通して自然と工芸の交差点に足を踏み入れ、藍染文化の無限の可能性を探求しましょう！📖💙✨")]
                )
            )
        elif text == '아름다움을염색하다소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="작은 그림책, 큰 색채: 함께 인디고 염색 문화의 아름다움을 탐구해요! 📖💙✨\\n인디고 염색은 자연과 장인의 기술이 결합된 것이자, 전통 공예와 생활 예술의 표현입니다. 하나의 식물 잎에서 시작하여 발효, 염색, 건조 과정을 거쳐 따뜻하고 깊은 푸른색으로 변합니다. 인디고 염색은 기술의 전수일 뿐만 아니라 사람들의 삶에 녹아들어 자연의 리듬과 문화적 깊이를 상징합니다.\n이 귀중한 공예를 더 많은 사람들에게 알리기 위해, 우리는 교육과 예술을 결합한 그림책을 제작했습니다. 이야기를 통해, 그리고 매력적인 삽화를 통해 독자들이 인디고 염색 문화의 매력을 경험할 수 있도록 했습니다. 💚\n\n인디고 향기와 책의 향기가 퍼져나가며, 이 그림책을 통해 자연과 공예가 교차하는 세계로 들어가 인디고 염색 문화의 무한한 가능성을 탐구해 봅시다! 📖💙✨")]
                )
            )
        elif text == '綠色足跡簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「小小繪本，大大行動，一起守護地球未來！📖🌍🌱」\n\n碳足跡，不僅是現代生活的無形記錄，更是我們對地球的承諾與責任。\n為了讓更多人了解碳足跡的概念及其對環境的影響，我們創作了一本充滿教育意義與藝術魅力的繪本。透過感人的故事與細膩的插畫，帶領讀者探索碳足跡背後的環保課題💚。\n碳足跡繪本以淺顯易懂的方式，幫助大小朋友認識減少碳排放的重要性，同時提供簡單可行的生活改變建議。從小改變開始，共同邁向永續的未來！🌿🌍📖\n\n與書香共行，讓我們一起為地球的美好盡一份心力！")]
                )
            )
        elif text == 'GreenFootprintIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'A Small Picture Book, a Big Action—Let's Protect the Future of Our Planet Together! 📖🌍🌱'\n\nCarbon footprints are not just invisible traces of modern life; they represent our responsibility and commitment to the Earth.\nTo help more people understand the concept of carbon footprints and their impact on the environment, we created an educational and artistic picture book. Through heartfelt storytelling and detailed illustrations, readers are guided to explore the environmental issues behind carbon footprints. 💚\nThis picture book uses simple language to teach both children and adults the importance of reducing carbon emissions, offering practical and achievable tips for everyday changes. Start small, and together, let's move toward a sustainable future! 🌿🌍📖\n\nLet the aroma of knowledge guide us—join us in making the world a better place for all!")]
                )
            )
        elif text == '綠の足跡紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「小さな絵本、大きな行動—未来の地球を一緒に守りましょう！📖🌍🌱」\n\nカーボンフットプリントは、現代生活の見えない足跡であるだけでなく、地球への責任と約束でもあります。\nこの概念と環境への影響をより多くの人に理解してもらうために、教育と芸術が融合した絵本を制作しました。感動的な物語と繊細なイラストを通じて、カーボンフットプリントの背後にある環境問題を探ります💚。\n\nこの絵本は、簡単な言葉で子どもから大人まで、炭素排出削減の重要性を伝え、日常生活で実行可能なアドバイスを提供します。小さな変化から始めて、持続可能な未来に向かって一緒に歩みましょう！🌿🌍📖\n\n知識の香りを共に楽しみながら、より良い世界を目指しましょう！")]
                )
            )
        elif text == '녹색발자국소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="'작은 그림책, 큰 실천—함께 지구의 미래를 지켜요! 📖🌍🌱'\n\n탄소 발자국은 현대 생활의 보이지 않는 흔적일 뿐만 아니라, 지구에 대한 우리의 책임과 약속입니다.\n탄소 발자국의 개념과 환경에 미치는 영향을 더 많은 사람들이 이해할 수 있도록, 교육과 예술이 결합된 그림책을 제작했습니다. 감동적인 이야기와 세밀한 삽화를 통해 탄소 발자국 뒤에 숨겨진 환경 문제를 탐구합니다💚.\n이 그림책은 아이부터 어른까지 누구나 이해하기 쉬운 언어로 탄소 배출 감소의 중요성을 전달하며, 일상에서 실천 가능한 간단한 팁을 제공합니다. 작은 변화에서 시작해 지속 가능한 미래를 향해 함께 나아가요! 🌿🌍📖\n\n지식의 향기를 함께 느끼며, 더 나은 세상을 만들어 갑시다!")]
                )
            )
        elif text == '茶鄉故事':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'TeaVillageStory':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '그림책세계에들어가다':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '茶の里の物語':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '陶藝物語':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'CeramicArtTale':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '도예이야기':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '陶芸の物語':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '染出美好':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '아름다움을염색하다':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'DyeingBeauty':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == '美しさを染める':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
        elif text == 'LinePlay簡介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「尋找文化碎片，重拾遺失的故事📖！」\n\n我們為碳足跡以及三大文化做了一款情境遊戲，由吉祥物小鶯帶你們一起進入永續之旅，幫助他找回文化碎片🧩，透過引人入勝的劇情，遊玩者將能更深刻地體會和共鳴，達到身歷其境的效果。🥰\n\n🎮遊玩須知\n📍請先下載Popworld App\n📍若想重新遊玩，請輸入重開碼\n中：75GS7\n英：21N3K\n\n🔗App\n中：https://reurl.cc/nqpYG8\n英：https://reurl.cc/36k2R0\n\n盡情享受這趟充滿意義的永續旅程，和小鶯藝起探索文化的魅力吧！🫵🏻")]
                )
            )
        elif text == 'LinePlayIntroduction':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「Discover cultural fragments and reclaim lost stories 📖！」\n\nWe have created a scenario game focusing on carbon footprints and three major cultures, where the mascot, Little Ying, takes you on a sustainable journey to help retrieve cultural fragments 🧩. Through an engaging storyline, players will gain a deeper understanding and resonance, achieving an immersive experience. 🥰\n\n🎮 Game Instructions\n📍 Please download the Popworld App first\n📍 If you want to replay, please enter the reset code.\nCH：75GS7\nEN：21N3K\n\n🔗 App\nCH: https://reurl.cc/nqpYG8\nEN: https://reurl.cc/36k2R0\n\nEnjoy this meaningful sustainable journey and explore the charm of culture with Little Ying! 🫵🏻")]
                )
            )
        elif text == 'Lineplay소개':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「문화 조각을 찾아 잃어버린 이야기를 되찾아보세요 📖！」\n\n우리는 탄소 발자국과 세 가지 주요 문화를 중심으로 한 시나리오 게임을 제작했습니다. 마스코트인 작은 잉이 여러분을 지속 가능한 여행으로 안내하여 문화 조각을 되찾는 데 도움을 줍니다 🧩. 매력적인 스토리를 통해 플레이어는 더 깊은 이해와 공감을 얻어 몰입할 수 있는 경험을 하게 됩니다. 🥰\n\n🎮 게임 안내\n📍 먼저 Popworld App을 다운로드하세요\n📍 재플레이를 원하시면 재시작 코드를 입력하세요.\nCH：75GS7\nEN：21N3K\n\n🔗 앱\nCH: https://reurl.cc/nqpYG8\nEN: https://reurl.cc/36k2R0\n\n의미 있는 지속 가능한 여행을 즐기고 작은 잉과 함께 문화의 매력을 탐험해보세요! 🫵🏻")]
                )
            )
        elif text == 'LinePlay紹介':
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="「文化の断片を探し、失われた物語を取り戻そう 📖！」\n\n私たちは、カーボンフットプリントと三大文化に焦点を当てた没入型ゲームを作成しました。マスコットのシャオインがあなたを持続可能な旅に導き、文化の断片を取り戻す手助けをします 🧩。魅力的なストーリーを通じて、プレイヤーは深く共感し、実体験を得ることができるでしょう。 🥰\n\n🎮 ゲームの注意事項/n📍 まず、Popworldアプリをダウンロードしてください。\n📍 再プレイしたい場合は、リセットコードを入力してください。\nCH: 75GS7\nEN: 21N3K\n\n🔗 アプリ\nCH: https://reurl.cc/nqpYG8\nEN: https://reurl.cc/36k2R0\n\n意味のある持続可能な旅を楽しみ、シャオインと一緒に文化の魅力を探求してください！ 🫵🏻")]
                )
            )
        elif text == '차마을이야기':#日文richmenu介面
            line_flex_json = open(f"./static/{text}.json", 'r', encoding='utf-8').read()
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_json))]
                    )
                )
                   
        else:
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=event.message.text)]
                )
            )
        
if __name__ == "__main__":
    app.run()