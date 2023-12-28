import discord #download 
from discord.ext import commands, tasks #download
from pytube import YouTube #download
import json
import schedule #download
from os import remove

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

forpause:discord.VoiceClient = None # this variable for keep state 
checkIsnotPlay = 0 #for check bot not play something within 1 minute 

@bot.event
async def on_ready():
    print('!!!Bot online!!!')
    check_schedule.start()
    

def job():
    global forpause
    global checkIsnotPlay
    print('working!!!')
    if forpause is not None:
        if forpause.is_playing() == False:
            checkIsnotPlay += 1
            print(checkIsnotPlay)
        else:
            checkIsnotPlay = 0
    if checkIsnotPlay == 2: # bot not play song or sound within 1 minute then exit
        checkIsnotPlay = 0
        forpause = None
        bot.loop.create_task(leave_voice_channel())

         
async def leave_voice_channel():
    for vc in bot.voice_clients:
        await vc.disconnect()

schedule.every(30).seconds.do(job)

@tasks.loop(seconds=1)
async def check_schedule():
    schedule.run_pending()


@bot.event
async def on_message(message: discord.Message):
    message_content = message.content
    if message_content.startswith('/play'):

        url = message_content.split()[1]

        #download file video into server
        youtube = YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        audio_stream.download(filename='play.wav', output_path='youtube_music')
        # duration = youtube.length #time file video

        global forpause
        if forpause == None:
            #connect bot to room 
            voicechannel = await message.author.voice.channel.connect()
            forpause = voicechannel
            playing = discord.FFmpegPCMAudio('youtube_music/play.wav', options='-vn')

            #play music
            voicechannel.play(playing)

        elif forpause.is_connected() and forpause is not None:
            forpause.stop()
            playing = discord.FFmpegPCMAudio('youtube_music/play.wav', options='-vn')
            forpause.play(playing)

    elif message_content.startswith('/pause'):
        forpause.pause()

    elif message_content.startswith('/resume'):
        forpause.resume()

    elif message_content.startswith('/stop'):
        forpause.stop()

    elif message_content.startswith('/dis'):
        forpause.stop()
        await forpause.disconnect()
        forpause = None
    
    elif message_content.startswith('/join'):
        voicetest = await message.author.voice.channel.connect()
        forpause = voicetest
    
    elif message_content.startswith('/opsong'):

        mess_args = message_content.split()[1:]
        id_discord = str(message.author.id)
        json_ = ReadWriteJson('data.json')
        if mess_args[0] == 'enable' and len(message.attachments) == 1:
            att = message.attachments[0]
            # download file from discord server
            await att.save(f'opsong/{att.filename}')


            data_json = json_.readfilejson()
            if id_discord not in data_json['users']['id']:
                json_.firstenablesong(id_discord, att.filename)

            else:
                old_pathfile = data_json['users']['id'][id_discord]['pathfile']

                #remove old file
                try:
                    remove(f'opsong/{old_pathfile}')
                except FileNotFoundError:
                    #send file not found into server discord
                    await message.channel.send('FILE NOT FOUND')
                except Exception as e:
                    #show error 
                    print(e)

                # write json file
                json_.writefilejson(id_discord=id_discord, args=mess_args[0], filename=att.filename)
            
            #download finish and ready to play
            await message.channel.send("DOWNLOAD FINISHED")

        elif mess_args[0] == 'disable':

            data_json = json_.readfilejson()
            old_pathfile = data_json['users']['id'][id_discord]['pathfile']

            #remove old file
            try:
                remove(f'opsong/{old_pathfile}')
            except FileNotFoundError:
                #send file not found into server discord
                await message.channel.send('FILE NOT FOUND')
            except Exception as e:
                #show error 
                print(e)

            # write json file
            json_ = ReadWriteJson('data.json')
            json_.writefilejson(id_discord=id_discord, args=mess_args[0])

    elif message_content.find('cum') >= 0:
        await message.channel.send('BOT GONNA CUM')
    
    await bot.process_commands(message)

class ReadWriteJson:
    def __init__(self, file) -> None:
        self.file = file

    def readfilejson(self):
        with open(self.file, encoding='utf8') as f:
            t = f.read()
        d = json.loads(t)
        return d
    
    def firstenablesong(self, id_discord, filename):
        file = self.readfilejson()

        file['users']['id'][id_discord] = {"opsong_enable": True, "pathfile": filename}

        save = json.dumps(file)
        with open('data.json', mode='w', encoding='utf8') as f:
            f.write(save)

    def writefilejson(self, args, id_discord, filename=None):
        file = self.readfilejson()
        if args == 'enable':
            file['users']['id'][id_discord]['opsong_enable'] = True
            file['users']['id'][id_discord]['pathfile'] = filename

        elif args == 'disable':
            file['users']['id'][id_discord]['opsong_enable'] = False
            file['users']['id'][id_discord]['pathfile'] = ""

        save = json.dumps(file)
        with open('data.json', mode='w', encoding='utf8') as f:
            f.write(save)

@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):

    global forpause
    if before.channel is None and after.channel is not None and not member.bot:

        room_id = member.voice.channel.id
        member_id = str(member.id)

        jSon = ReadWriteJson('data.json')        
        dict_json = jSon.readfilejson()

        #You are not set your opsong
        if member_id not in dict_json['users']['id']:
            return

        pathfile = dict_json['users']['id'][member_id]['pathfile']
        enable = dict_json['users']['id'][member_id]['opsong_enable']

        #check opsong enable if true then play
        if enable == False:
            return

        if forpause is not None:
            if forpause.is_connected() == True:

                forpause.stop()                
                playing = discord.FFmpegPCMAudio(f'opsong/{pathfile}', options='-vn')
                forpause.play(playing)

        else:
            voicechannel = await member.voice.channel.connect()    
            forpause = voicechannel
            playing = discord.FFmpegPCMAudio(f'opsong/{pathfile}', options='-vn')
            forpause.play(playing)

    elif before.channel is not None and after.channel is None:
        pass


jSon = ReadWriteJson('data.json')        
token = jSon.readfilejson()['token']
bot.run(token)


