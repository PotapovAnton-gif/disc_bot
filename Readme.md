## DISCORD BOT FOR TRELLO NOTIFICATIONS

This bot is about coonect to your trello board, get the changes and send it to
    your chat

You shold activate some things, first of all you have to create your 
    pesonal api_key, api-secrt and token. More information about this [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)

Also you need to activate [developer mod](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/) to your discord
    account and take chennel id for bot. Then go and set up [token](https://tproger.ru/articles/sozdajom-discord-bota-na-python/#:~:text=%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D1%91%D0%BC%20%D0%BD%D0%B0%D1%88%D0%B5%D0%B3%D0%BE%20%D0%B1%D0%BE%D1%82%D0%B0,%D0%94%D0%B0%D0%BB%D1%8C%D1%88%D0%B5%20%D0%BE%D0%BD%20%D0%BD%D0%B0%D0%BC%20%D0%BF%D0%BE%D0%BD%D0%B0%D0%B4%D0%BE%D0%B1%D0%B8%D1%82%D1%81%D1%8F!) for your bot
      

You need to create files:

config.py = {
    
    api_key = "your_trello_api_key" - string
    api_secret = "your_trello_api_secret" - string
    token = "your_trello_token" - string
    board_id = "your_trello_board_id" - string

    channel_id = your_discord_channel_id - int
    bot_token = "your_discord_bot_token" - string

}

users.yml = {

    user_id_trello : "<@discord_id>"

}

db.yml = {

    last_activity = "" - str 

}

# usage 

run following commands to start your bot in docker  

run : sudo docker build -t your_name_of_image /your/path/to/disc_bot

run : sudo docker run -d --name your_name_of_container your_name_of_image



For questions write to me at:

tg : @JastAnt
email: antpotapov2019@gmail.com
