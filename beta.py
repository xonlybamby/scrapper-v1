import asyncio
import aiohttp
from telethon import TelegramClient, events

# Coloca aquí tus credenciales de API y el número de chat al que quieres reenviar los mensajes
API_ID = ''
API_HASH = ''
SEND_CHAT = ''

# Inicializa el cliente de Telegram
client = TelegramClient('session', API_ID, API_HASH)

# Define los chats en los que quieres escuchar los mensajes
CHATS = [
    '@Aqui los chats',
]

#
## Crea un manejador de eventos para los mensajes editados que cumplan las condiciones
@client.on(events.MessageEdited(chats=CHATS, incoming=True, func=lambda x: x.text and '✅' in x.text and '❌' not in x.text and ('Approved' in x.text or 'APPROVED' in x.text or 'Aproved' in x.text or 'CHARGED 0.01$' in x.text or '🟩' in x.text or '**[ APPROVED ✅ ]**' in x.text or '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱' in x.text or '𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅' in x.text)))
async def handle_edited_message(event):
    # Espera un poco antes de reenviar el mensaje
    await asyncio.sleep(0.1)
    # Crea un botón con una URL76489
    
    message_text = f"{event.text}\n \n[Owner the scrapp](https://t.me/aboutbamby)"
    # Reenvía el mensaje a un  canal específico
    await client.send_message(SEND_CHAT, message_text, link_preview=False)


# Función para verificar la conexión a internet
async def check_internet_connection():
    try:
        async with aiohttp.ClientSession() as session:
            await session.get('http://www.google.com')
    except aiohttp.ClientError:
        return False 
    return True




# Función principal para iniciar sesión y ejecutar el bucle de eventos
async def main():
    # Espera hasta que haya una conexión a internet disponible
    while not await check_internet_connection():
        await asyncio.sleep(1)

    # Inicia sesión en Telegram
    await client.start()
    await client.run_until_disconnected()


try:
    # Ejecuta el bucle principal
    asyncio.run(main())
except KeyboardInterrupt:
    # Manejo de la interrupción del teclado (Ctrl+C)
    print("Se presionó Ctrl+C. El programa se cerró.")