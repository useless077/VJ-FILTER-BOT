# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @Tamilbots
# Ask Doubt on telegram @TamilSupport

from pyrogram import filters,Client
from info import LOG_CHANNEL as LOG_GROUP, REQST_CHANNEL as DUMP_GROUP
import os,re,asyncio,bs4
import requests,wget,traceback

@Client.on_message(filters.regex(r'https?://.*twitter[^\s]+') & filters.incoming | filters.regex(r'https?://(?:www\.)?x\.com/\S+') & filters.incoming,group=-5)
async def twitter_handler(Client, message):
   try:            
      link=message.matches[0].group(0)
      if "x.com" in link:
         link=link.replace("x.com","fxtwitter.com")
      elif "twitter.com" in link:
         link = link.replace("twitter.com","fxtwitter.com")
      m=await message.reply_sticker("CAACAgIAAxkBATWhF2Qz1Y-FKIKqlw88oYgN8N82FtC8AAJnAAPb234AAT3fFO9hR5GfHgQ")
      try:
          dump_file = await message.reply_video(link,caption="Thank you for using - @TamilMovies5K")
      except Exception as e:
          print(e)
          try:
             snd_message=await message.reply(link)
             await asyncio.sleep(1)
             dump_file = await message.reply_video(link,caption="Thank you for using - @TamilMovies5K")
             await snd_message.delete()
          except Exception as e:
              print(e)
              await snd_message.delete()
              get_api=requests.get(link).text
              soup=bs4.BeautifulSoup(get_api,"html.parser")
              meta_tag= soup.find("meta", attrs = {"property": "og:video"})
              if not meta_tag:
                  meta_tag = soup.find("meta", attrs={"property": "og:image"})
              content_value  = meta_tag['content']
              try:
                  dump_file = await message.reply_video(content_value,caption="Thank you for using - @TamilMovies5K")
              except Exception as e:
                  print(e)
                  try:
                     snd_msg=await message.reply(content_value)
                     await asyncio.sleep(1)
                     await message.reply_video(content_value,caption="Thank you for using - @TamilMovies5K")
                     await snd_msg.delete()
                  except Exception as e:
                      print(e)
                      await message.reply("Oops Invalid link or Media Is Not Available:)")
   except Exception as e:
        print(e)
        if LOG_GROUP:
           await Client.send_message(LOG_GROUP,e)
           await Client.send_message(LOG_GROUP,traceback.format_exc())
   finally:
       if DUMP_GROUP:
          if "dump_file" in locals():
             await dump_file.copy(DUMP_GROUP)
       await m.delete()
       await message.reply("Check out @TamilMovies5k (music)  @TamilBots(Channel) \n Please Support Us By /donate To Maintain This Project")               
                  
