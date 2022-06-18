from statistics import mode
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

        self.possible_actions = {

        "createCard" : "создана карточка",
        "updateCard" : "перемещена карточка",
        "deleteCard" : "удалена карточка",
        "updateCheckItemStateOnCard" : "обновлено состояние карточки",
        "commentCard" : "добавлен комментарий в карточке",
        "addChecklistToCard" : "добавлен чек-лист в карточке",
        "addMemberToCard" : "добавлен участник к карточке",
        "makeAdminOfBoard" : "добавлен администратор доски",
        "removeMemberFromCard" : "удален участник с карточки",
    
        }
    

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
            
            with open("db.yml", 'w') as db:
                yaml.safe_dump(self.db, db, default_flow_style=False)            

            action = self.get_action("all")
            type_action = self.possible_actions.get(action.get("type"))    
            creator = self.users.get(
                action.get("memberCreator").get("id")
                )
            
            try:
                name_of_card = action.get('data').get('card').get('name')
            except:
                name_of_card = "Никакая("
            
            users = self.get_users(
                action.get('data').get('card').get('id')
                )
            try:
                list = action.get('data').get('listAfter').get("name")
            except:
                list = action.get('data').get("list").get("name")      
            
            
            message1 = f"Свершилось чудо: {type_action}," 
            message3 = f"этим прекрасным человеком: {creator} (огромное ему спасибо за работу),"
            message2 = f" с имяшкой: {name_of_card}, в колоночку: {list}, "
            message4 = "не позавидуешь:"
            try:
                for i in users:
                    message4 += " " + self.users[i]
            
            except:
                None
            return message1 + message2 + message3 + message4
            





if __name__ == "__main__":
    trel = Trwork()
    
    while True:
        message = trel.get_message()
        if message is not None:
            print (message)





       


#createCard updateCard deleteCard
        
    
        
        

    



