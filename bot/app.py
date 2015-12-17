import os
import sys
import time

import telepot


ACCESS_TOKEN = os.getenv("TELEGRAM_API_KEY")

if not ACCESS_TOKEN:
    exit()

file_name = 'last-post-id.txt'
group_id = -1001005702961
last_post_id = int(sys.argv[1] if len(sys.argv) > 1 else open(file_name).readline())


bot = telepot.Bot(ACCESS_TOKEN)

while True:
    try:
        bot.forwardMessage(group_id, '@addmeto', last_post_id + 1)

        last_post_id += 1

        with open(file_name, 'w') as f:
            f.write(str(last_post_id))
    except telepot.TelegramError:
        pass

    time.sleep(10)
