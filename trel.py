from typing import List, Dict
from trello import TrelloClient
import yaml
from config import api_key, api_secret, token, board_id

class Trwork:
    def __init__(self):
        
     
        self.client = TrelloClient(
                api_key = api_key,
                api_secret=api_secret,
                token = token,
    )

        self.board = self.client.get_board(board_id)
        
        with open('db.yml', 'r') as db:
            self.db = yaml.safe_load(db)

        with open('users.yml') as us:

            self.users = yaml.safe_load(us)
    

    def get_action(self, acfiltr:str) -> Dict:
        
        action = self.board.fetch_actions(
            action_filter=acfiltr, action_limit=1
        )[0]

        return action

    def get_users(self, targ_id) -> List:
        self.cards = self.board.get_cards()
        for i in self.cards:
            if i.id == targ_id:
                return i.idMembers
    

    def get_message(self) -> str:

        if not (str(self.board.get_last_activity()) == self.db[
                                                        "last_activity"]
                                                        ):
            
            self.db["last_activity"] = str(self.board.get_last_activity())
            quat_cards = len(self.board.all_cards())
            
            if self.db["quan_cards"] < quat_cards:
                self.db["quan_cards"] = quat_cards
                
                with open("db.yml", 'w') as db:
                    yaml.safe_dump(self.db, db, default_flow_style=False)
                
                action = self.get_action("createCard")
                creator = action.get("memberCreator").get("id")
                name_of_card = action.get('data').get('card').get('name')
                users = self.get_users(action.get('data').get('card').get('id'))
                list = action.get("data").get("list").get("name")    
                
                message = f"Была добавлена карточка пользователем: {self.users.get(creator)}, с именем: {name_of_card}, в колонку: {list}, прикреплены пользовалели:"
                try:
                    for i in users:
                        message += " " + self.users[i]
                
                except:
                    KeyError
                return message
            
            elif self.db["quan_cards"] == quat_cards:
                
                with open("db.yml", 'w') as db:
                    yaml.safe_dump(self.db, db, default_flow_style=False)

                action = self.get_action("updateCard")
                creator = action.get("memberCreator").get("id")
                name_of_card = action.get('data').get('card').get('name')
                users = self.get_users(action.get('data').get('card').get('id'))
                try:
                    list = action.get('data').get('listAfter').get("name")
                except:
                    list = action.get('data').get("list").get("name")    
                
                message = f"Была перемещена карточка пользователем: {self.users.get(creator)}, с именем: {name_of_card}, в колонку: {list}, прикреплены пользовалели:"
                try:
                    for i in users:
                        message += " " + self.users[i]
                
                except:
                    KeyError
                return message

            
            else: 
                self.db["quan_cards"] = quat_cards

                with open("db.yml", 'w') as db:
                    yaml.safe_dump(self.db, db, default_flow_style=False)

                action = self.get_action("deleteCard")
                creator = action.get("memberCreator").get("id")
                name_of_card = action.get('data').get('card').get('name') 
                list = action.get("data").get("list").get("name")    
                
                message = f"Была удалена карточка пользователем: {self.users.get(creator)}, из колонки: {list}"
                return message





if __name__ == "__main__":
    trel = Trwork()
    
    
    while True:
        message = trel.get_message()
        if message is not None:
            print (message)





       


#createCard updateCard deleteCard
        
    
        
        

    



