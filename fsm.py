from transitions.extensions import GraphMachine
from utils import send_text_message
from crawler import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_ranking(self, event):
        text = event.message.text
        return text == 'ranking'

    def on_enter_ranking(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter a number(1-100)")

    def is_going_to_players(self, event):
        text = event.message.text
        return text == 'players'
    
    def on_enter_players(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter a player's name")

    def is_going_to_tournaments(self, event):
        text = event.message.text
        return text == 'tournaments'

    def on_enter_tournaments(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter a number(1-12)")

    def is_going_to_headtohead(self, event):
        text = event.message.text
        return text == "head to head"

    def on_enter_headtohead(self, event):
        print("I'm entering H2H")
        reply_token = event.reply_token
        send_text_message(reply_token, "enter two player(player1 vs player2):")

    def is_going_to_getranking(self, event):
        text = event.message.text
        return text.isdigit()

    def on_enter_getranking(self, event):
        reply_token = event.reply_token
        rank = int(event.message.text)
        if 1 <= rank <= 100:
            send_text_message(reply_token, str(nameList[rank-1]))  
        else:
            send_text_message(reply_token, "number must in [1, 100]")
        self.go_back()
    
    def is_going_to_getplayername(self, event):
        text = event.message.text
        return text.title() in nameList

    def on_enter_getplayername(self, event):
        reply_token = event.reply_token
        text = event.message.text
        name = changeformat(text)
        playerinfo = getplayerinformation(name, imformation[text.title()])
        print(playerinfo)
        reply = ""
        for k, v in playerinfo.items():
            reply += "%s : %s\n\n"%(k, v)
        send_text_message(reply_token, reply[:-2])
        self.go_back()

    def is_going_to_gettournaments(self, event):
        text = event.message.text
        return text.isdigit()

    def on_enter_gettournaments(self, event):
        reply_token = event.reply_token
        text = event.message.text
        reply = gettournamentinformation(text)
        send_text_message(reply_token, reply)
        self.go_back()

    def is_going_to_getheadtohead(self, event):
        text = event.message.text
        player = text.split(" vs ")
        print(player)
        return player[0].title() in nameList and player[1].title() in nameList

    def on_enter_getheadtohead(self, event):
        reply_token = event.reply_token
        text = event.message.text
        reply = getheadtoheadinfomation(text)
        send_text_message(reply_token, reply)
        self.go_back()
        
    def is_going_to_back_to_user(self, event):
        text = event.message.text
        return text == "back to user"
    

   
    

    
    
    