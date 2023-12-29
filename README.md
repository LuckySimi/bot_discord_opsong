# Installation


### Vscode
#### for coding in vscode
```
    git clone https://github.com/LuckySimi/bot_discord_opsong.git
```
#### requirements
    python version 3.10.11
```
    pip install -r requirements.txt
```

### ffmpeg
  install this in your computer because this use for run your program
##### Windows
if you use windows don't forgot set environment ffmpeg

[Windows](https://ffmpeg.org/download.html#build-windows)
##### MacOs
[MacOs](https://ffmpeg.org/download.html#build-mac)
##### Linux
[Linux](https://ffmpeg.org/download.html#build-linux)

### CREATION BOT DISCORD
#### Select new application !!!
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/88c3064d-467e-4060-9116-4c76a7179301)
#### Enter your name !!!
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/b05b294e-6cd2-4843-aad2-8ba12dc5116c)
#### Select BOT !!!
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/86eb0179-c4f6-40ec-ab6c-bb6a6eddabad)

#### Setting Privileged Gateway Intents
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/8e365f49-7560-4f9c-8080-6c6e37643052)

#### Go to BOT and setting select bot and permission is admin
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/04032c20-e434-4673-a687-22a1a42663e1)

#### Go to OAuth and keep your link for invite your bot connect yourserver
copy link into url and invite your bot 
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/abcdd5f8-66aa-4de9-bb96-51d3f6780e7e)

#### Select reset token and keep your token
![image](https://github.com/LuckySimi/bot_discord_opsong/assets/153023501/5bbd9775-89a6-4304-b93e-d19b63b0eebe)

### Token
#### Open your data.json file then put your token into "Your token"

```json
     {
    "users": {
        "id": {
            
        }
    },
    "token": "Your token"
    }
```

### Run your code

```python
    python botdiscord.py
```

# Docker

### Token
#### Open your data.json file then put your token into "Your token"

```json
     {
    "users": {
        "id": {
            
        }
    },
    "token": "Your token"
    }
```

### BUILD DOCKER AND RUN
```docker
    docker build -t image_namebot_discord .
    docker run --name name_contrainer -d image_namebot_discord
```


