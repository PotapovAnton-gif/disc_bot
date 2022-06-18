## DISCORD BOT FOR TRELLO NOTIFICATIONS

This bot is about coonect to your trello board, get the changes and send it to your chat

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
    user_id_trello : "@discrod_username"
}

db.yml = {
    last_activity = "" - str
    quan_cards = 0 - int 
}

