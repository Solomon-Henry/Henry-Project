from general import *
from Location_Data import Location_Dict
from location import Location
from world import World

class Player:
    score = 0
    def update_player_count(Player):
        player_list.append(Player)
    def __init__(Player):
        Player.update_player_count()
        Player.name = ""
        Player.world = World()
        Player.location_id = 0
        Player.move_count = 0
        Player.points = 0
        Player.Death_Status = False
        Player.Quit_Status = False
    def update_save_data(Player):

        pass
    def get_name(Player):
        return Player.name
    def set_status(Player,type):
        if type == "DEATH":
            Player.Death_Status = True
        elif type == "QUIT":
            Player.Quit_Status = True
    def set_name(Player,name):
        Player.name = name
    def get_score(Player):
        return Player.score
    def display_progress(Player):
        if Location_Dict[Player.location_id].get("Was_Visited") == False:
            Player.points += 15
            Location_Dict[Player.location_id]["Was_Visited"] = True
        Player.move_count += 1
        Story_Progress = (Player.move_count/10) * 100
        print(f"\nStory Progress: {Story_Progress}%\nTotal Score: {Player.points} points")
        
        
    def game_loop(Player):
        for location_id in range(10):
            Player.move(location_id)
        Player.ending()
    def move(Player,jump=-1,display=True):
        if not Player.Death_Status and not Player.Quit_Status:
            if jump == -1:
                Player.world.update_location()
            else: 
                Player.world.update_location(jump)
            Player.location_id = Player.world.get_location("ID")
            location_list[Player.location_id].Script_Runner()
            if display:
                Player.display_progress()
    def ending(Player):
        if Player.Death_Status:
            #Death ending
            Player.move(12,False)
            pass
        elif Player.Quit_Status:
            #Quit ending
            Player.move(13,False)
            pass
        else: 
            #Good Ending
            Player.move(11,False)
            pass
        Player.restart()
        pass
    def restart(Player):
        restart_prompt = input("\nYou can restart by typing 'yes' or quit by pressing enter here: ")
        if restart_prompt == "Yes" or restart_prompt == "yes": 
            Player.Death_Status = False
            Player.Quit_Status = False
            Player.Finish_Status = False
            Player.move_count = 0
            Player.game_loop()
        else:
            #Good Ending
            input("\nGreat job on finishing my game. Hope you enjoyed my project!")
            