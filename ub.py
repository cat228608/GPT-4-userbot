from telethon import TelegramClient, events, sync
import g4f

api_id = '11111' #ваш api id
api_hash = 'd2858df886e5b3' #ваш api hash
session_name = 'session'

client = TelegramClient(session_name, api_id, api_hash)

async def chatgpt(query):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": query}],
        )
        return response
    except Exception as e:
        print(e)
        return 'Ошибка при генерации!'

@client.on(events.NewMessage(pattern='/otvet'))
async def respond_to_message(event):
    if event.is_reply:
        message = await event.get_reply_message()
        try:
        	await event.edit("Ща погоди...")
        	result = await chatgpt("Ответь на сообщение будто ты человек которого зовут (ваше имя) и ты хорошо разбираешься в айти, отвечай молодежно и старайся чделатл так что бы твой ответ не был похож на ответ нейросети!\nВопрос: " + message.text)
        	await event.edit(result)
        except Exception as e:
        	print(e)
        	pass

@client.on(events.NewMessage(pattern='/chat'))
async def handle_chat(event):
    try:
    	await event.edit("Думаю что ответить...")
    	args = event.text.split('/chat ')[1]
    	result = await chatgpt(args)
    	await event.edit(f"Ваш запрос: {args}\n\nGPT4: " + result)
    except Exception as e:
    	print(e)
    	pass

with client:
    client.run_until_disconnected(
