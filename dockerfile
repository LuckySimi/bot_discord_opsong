FROM python:3.10.13

WORKDIR /usr/src/app

COPY youtube_music ./youtube_music
COPY opsong ./opsong
COPY ./data.json ./
COPY ./botdiscord.py ./

RUN pip install pytube==15.0.0
RUN pip install schedule==1.2.1
RUN pip install discord.py==2.3.2
RUN pip install PyNaCl==1.5.0
RUN apt-get update 
RUN apt-get install ffmpeg -y

CMD [ "python", "botdiscord.py"]