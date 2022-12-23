from fsm import TocMachine

def Mymachine():
    machine = TocMachine(
        states=["user", "ranking", "getranking", "players", "getplayername", "headtohead", "getheadtohead", "tournaments", "gettournaments"],
        transitions=[
            {
                "trigger": "advance", 
                "source": "user", 
                "dest": "ranking", 
                "conditions": "is_going_to_ranking"
            },
            {
                "trigger": "advance", 
                "source": "user", 
                "dest": "tournaments", 
                "conditions": "is_going_to_tournaments"
            },
            {
                "trigger": "advance", 
                "source": "ranking", 
                "dest": "getranking", 
                "conditions": "is_going_to_getranking"
            },
            {
                "trigger": "advance", 
                "source": "user", 
                "dest": "players", 
                "conditions": "is_going_to_players"
            },
            {
                "trigger": "advance", 
                "source": "user", 
                "dest": "headtohead", 
                "conditions": "is_going_to_headtohead"
            },
            {
                "trigger": "advance", 
                "source": "tournaments", 
                "dest": "gettournaments", 
                "conditions": "is_going_to_gettournaments"
            },
            {
                "trigger": "advance", 
                "source": "players", 
                "dest": "getplayername", 
                "conditions": "is_going_to_getplayername"
            },
            {
                "trigger": "advance", 
                "source": "headtohead", 
                "dest": "getheadtohead", 
                "conditions": "is_going_to_getheadtohead"
            },
            {
                "trigger": "advance", 
                "source": ["ranking", "getranking", "players", "getplayername", "headtohead", "getheadtohead", "tournaments", "gettournaments"], 
                "dest": "user", 
                "conditions": "is_going_to_back_to_user"
            },
            {
                "trigger": "go_back", 
                "source": "getranking", 
                "dest": "ranking"
            },
            {
                "trigger": "go_back", 
                "source": "getplayername", 
                "dest": "players"
            },
            {
                "trigger": "go_back", 
                "source": "getheadtohead", 
                "dest": "headtohead"
            },
            {
                "trigger": "go_back", 
                "source": "gettournaments", 
                "dest": "tournaments"
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine
