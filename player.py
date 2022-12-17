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
        Player.save_data = ""
        Player.Death_Status = False
        Player.Quit_Status = False
        Player.Load_File_Status = [False,""]
    def update_save_data(Player):
        Name = "Name: " + Player.name
        Location_ID = "Location_Id: " + str(Player.location_id)
        Move_count = "Move_Count: " + str(Player.move_count)
        Points = "Points: " + str(Player.points)
        save_data = Name + "\n" + Location_ID + "\n" + Move_count + "\n" + Points 
        Player.save_data = save_data
    def load_save_data(Player):
        data = Player.Load_File_Status[1]
        # Load new variables
        Player.name = data[0][6:]
        Player.location_id = int(data[1][13:])
        Player.move_count = int(data[2][12:])
        Player.points = int(data[3][8:])
    def get_name(Player):
        return Player.name
    def set_status(Player,type,data=""):
        if type == "DEATH":
            Player.Death_Status = True
        elif type == "QUIT":
            Player.Quit_Status = True
        elif type == "LOAD":
            Player.Load_File_Status[0] = True
            Player.Load_File_Status[1] = data
    def set_name(Player,name):
        Player.name = name
    def get_score(Player):
        return Player.points
    def display_progress(Player):
        if Location_Dict[Player.location_id].get("Was_Visited") == False:
            Player.points += 15
            Location_Dict[Player.location_id]["Was_Visited"] = True
        Player.move_count += 1
        Story_Progress = (Player.move_count/10) * 100
        display_prompt = input(f"\nStory Progress: {Story_Progress}%\nTotal Score: {Player.points} points")
        find_run_user_command(Player.location_id,Player,display_prompt)
        
    def game_loop(Player):
        Player.Load_File_Status = [False,""]
        game_loop_cnt = Player.location_id
        while game_loop_cnt < 10:
            Player.move(game_loop_cnt)
            game_loop_cnt += 1
        Player.ending()
    def move(Player,jump=-1,display=True):
        if not Player.Death_Status and not Player.Quit_Status and not Player.Load_File_Status[0]:
            if jump == -1:
                Player.world.update_location()
            else: 
                Player.world.update_location(jump)
            Player.location_id = Player.world.get_location("ID")
            Player.update_save_data()
            location_list[Player.location_id].Script_Runner()
            if display and not Player.Load_File_Status[0]:
                Player.display_progress()
            
    def ending(Player):
        if Player.Death_Status:
            #Death ending
            Player.Death_Status = False
            Player.move(12,False)
            pass
        elif Player.Quit_Status:
            #Quit ending
            Player.Quit_Status = False
            Player.move(13,False)
            pass
        elif Player.Load_File_Status[0]:
            Player.load_save_data()
            Player.game_loop()
            return None
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
            input("\nGreat job on finishing my game. Hope you enjoyed my project!")
            