from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters
import mysql.connector


bot = Client(session_name='Bot',
             api_hash='1b852557e771a37f4609749afeeeed78',
             api_id='427059',
             bot_token='2104577084:AAEt7_CldnJMWfmcxLJbc8Rhmhzi8heIr9E')


conn = mysql.connector.connect(user='root',
                               host='localhost',
                               database='Password_bot')

cursor = conn.cursor()

@bot.on_message(filters.command('start'))
async def Start(client, message):

    username = message.chat.username


    chat_id = message.chat.id

    Data = "SELECT username FROM users WHERE username = '{}'".format(username)

    cursor.execute(Data)

    result = cursor.fetchall()


    print(result)

    if result:

        for i in result:

            await bot.send_message(chat_id, f"""
@{username}

Welcome To Bot 
            
""")

    else:

        await bot.send_message(chat_id, f"""
@{username}


you don't have permission

""")

bot.run()