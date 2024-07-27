from telethon import TelegramClient,events

api_id = 21956425
api_hash = "0bd48fc8e98d6317def9baf6d69ac3d8"
phone_number = "+254790052730"

session_name = "wilson"

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats="@allsiga"))
async def my_event_handler(event):
#    print(event.text)
   message = event.text
   if('@' in message and 'buy' in message or 'sell' in message and 'tp' in message or 'sl' in message):
      print('this is a signal')
      for line in message.splitlines():
          if 'buy' in line:
              print('a buy signal')
          else:
              print('a sell signal')
      

client.start()
client.run_until_disconnected()
