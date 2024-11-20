# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @Tamilbots
# Ask Doubt on telegram @TamilSupport

from pyrogram import filters, Client
import bs4, requests,re,asyncio
import wget,os,traceback
from info import LOG_CHANNEL as LOG_GROUP, REQST_CHANNEL as DUMP_GROUP

@Client.on_message(filters.regex(r'https?://.*facebook[^\s]+') & filters.incoming,group=-6)
async def link_handler(Client, message):
    link = message.matches[0].group(0)
    try:
       m = await message.reply_text("⏳")
       get_api=requests.get(f"https://yasirapi.eu.org/fbdl?link={link}").json()
       if get_api['success'] == "false":
          return await message.reply("Invalid TikTok video url. Please try again :)")
       if get_api['success'] == "ok":
          if get_api.get('result').get('hd'):
             try:
                 dump_file = await message.reply_video(get_api['result']['hd'],caption="Thank you for using - @TamilMovies5K")
             except KeyError:
                 pass 
             except Exception:
                 try:
                     sndmsg = await message.reply(get_api['result']['hd'])
                     await asyncio.sleep(1)
                     dump_file = await message.reply_video(get_api['result']['hd'],caption="Thank you for using - @TamilMovies5K")
                     await sndmsg.delete()
                 except Exception:
                     try:
                        down_file = wget.download(get_api['result']['hd'])
                        await message.reply_video(down_file,caption="Thank you for using - @TamilMovies5K")
                        await sndmsg.delete()
                        os.remove(down_file)
                     except:
                         return await message.reply("Oops Failed To Send File Instead Of Link")
          else: 
             if get_api.get('result').get('sd'):
               try:
                   dump_file = await message.reply_video(get_api['result']['sd'],caption="Thank you for using - @TamilMovies5K")
               except KeyError:
                   pass
               except Exception:
                   try:
                       sndmsg = await message.reply(get_api['result']['sd'])
                       await asyncio.sleep(1)
                       dump_file = await message.reply_video(get_api['result']['sd'],caption="Thank you for using - @TamilMovies5K")
                       await sndmsg.delete()
                   except Exception:
                      try:
                        down_file = wget.download(get_api['result']['sd'])
                        await message.reply_video(down_file,caption="Thank you for using - @TamilMovies5K")
                        await sndmsg.delete()
                        os.remove(down_file)
                      except:
                         return await message.reply("Oops Failed To Send File Instead Of Link")
    except Exception as e:
           if LOG_GROUP:
               await Client.send_message(LOG_GROUP,f"Facebook {e} {link}")
               await Client.send_message(LOG_GROUP, traceback.format_exc())          
    finally:
          if 'dump_file' in locals():
            if DUMP_GROUP:
               await dump_file.copy(DUMP_GROUP)
          await m.delete()     
