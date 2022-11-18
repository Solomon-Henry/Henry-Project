from Location_Data import Location_Dict
from location import Location
from world import World

class Player:
    score = 0
    players = []
    User_Commands = ["EXAMINE","HELP","QUIT"]
    def update_player_count(Player):
        Player.players.append(Player)
    def __init__(Player,world):
        Player.update_player_count()
        Player.name = ""
        Player.world = world
        Player.location_id = 0
        Player.move_count = 0
        Player.points = 0
        Player.Death_Status = False
        Player.Quit_Status = False
        Player.Finish_Status = False
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
    def get_nearby_locations(Player):
        return Player.world.get_surrounding_locations()
    def display_progress(Player):
        if Location_Dict[Player.world.get_location("ID")].get("Was_Visited") == False:
            Player.points += 15
        Player.move_count += 1
        Story_Progress = (Player.move_count/10) * 100
        print(f"\nStory Progress: {Story_Progress}%\nTotal Score: {Player.move_count} points")
    def find_run_user_command(Player,str):
        if str.find(Player.User_Commands[0]):
            print("Examine Info: ")
            print(Player.world.get_location("INSTANCE"))
            input("\nPress Enter To Return To Story")
        elif str.find(Player.User_Commands[1]):
            print("Help info: ")
            print("\nValid Commands:\n\nEXAMINE: Find info on current location\nHELP: Display all valid commands\nQUIT: End game abruptly\n")
            input("Press enter To Return To Story")
        elif str.find(Player.User_Commands[2]):
            input("\nYou have quit the game.\nPress enter to continue to the end of the game :(")
            Player.Quit_Status = True
    def story_sequence(Player,num):
        for i in num:
            if Player.Finish_Status:
                break
            Current_Location = Player.world.get_location("INSTANCE")
            Current_Text_List = Location_Dict[Player.location_id].get("Text_List")
            for Text in Current_Text_List:
                if Player.Death_Status or Player.Quit_Status:
                    if Player.Death_Status:
                        Player.move(12)
                    elif Player.Quit_Status:
                        Player.move(13)
                    break
                print("****************************************")
                Current_Location.Script_Runner(Text)
                print("****************************************")
                if Current_Text_List.index(Text) == len(Current_Text_List)-1:
                    Player.display_progress()
        if not Player.Quit_Status and not Player.Death_Status:
            print("\nGreat job on finishing the game!")
        else:
            print("\nAww, you didn't finish the game. We the creators are very disappointed in you :(")
        if not Player.Finish_Status:
            Player.restart()
    def move(Player,jump=-1):
        if jump == -1:
            Player.update_location(1)
        else: 
            Player.update_location(jump)
    def restart(Player):
        restart_prompt = input("You can restart by typing 'yes' or quit by pressing enter here:")
        if restart_prompt == "Yes": 
            Player.world.update_location(0)
            Player.Death_Status = False
            Player.Quit_Status = False
            Player.Finish_Status = False
            Player.story_sequence()
        else:
            Player.move(10)
            Player.story_sequence()
            Player.Finish_Status = True