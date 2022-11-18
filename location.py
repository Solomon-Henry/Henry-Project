# To-Do add functionality to print out on text_lists and prompt user with choices
from player import Player
from Location_Data import Location_Dict
class Location:
    Text_Commands = ["TEXT","PROMPT","SET","CHOICE","|USERNAME|"]
    def Find_Execute_Command(str):
        command = str[str.index("|")+1:str[str.index("|")+1:].index("|")+str.index("|")+1]
        check_username = str.find(Location.Text_Commands[4])
        current_player = Player.players
        if check_username != -1:
            Text = Text[:check_username] + current_player.get_name() + Text[check_username+len(Location.Text_Commands[4]):]
        Text = str[len(command)+2:]
        if command == Location.Text_Commands[0]:
            print(Text)
            pass
        elif command == Location.Text_Commands[1]:
            user_input = input(Text)
            current_player.find_run_user_command(user_input)
            pass
        elif command == Location.Text_Commands[2]:
            user_input = input(Text)
            current_player.set_name(user_input)
            pass
        elif command == Location.Text_Commands[3]:
            option_ids = current_player.get_nearby_locations()
            options_text = []
            for id in option_ids:
                text = []
                text[0] = Location_Dict[id].get("Name") + ":"
                text[1] = "Location Info: " + Location_Dict[id].get("Examine")
                options_text.append(text)
            for option in options_text:
                for str in option:
                    print(f"\n{str}")
            user_prompt = "\nChoose one of the options above, i.e the corresponding name: "
            def check():
                response = input(user_prompt)
                options_name = []
                for id in option_ids:
                    options_name.append(Location_Dict[id].get("Name"))
                if not (response in options_name):
                    print("\nNo rushing! Please type in one of the options")
                    response = check()
                return response
            user_response = check()
            correct_response = Location_Dict[id+1].get("Name")
            if user_response == correct_response:
                print("\nGreat choice. You continue with your life.")
                input(Text)
            else: 
                input("\nBad decision, you will now be dead\nPress enter to continue ")
                current_player.set_status("DEATH")
                pass
            pass
        #Check for username regardless
        
        pass
    def Script_Runner(str):
        Location.Find_Execute_Command(str)
        pass
    def __init__(Location,name,info,text_list=""):
        Location.name = name
        Location.info = info
        Location.text_list = text_list
        Location.been_visited = False
    def __str__(Location):
        if Location.been_visited:
            print(f"You are at {Location.name}") 
        print(f"\n{Location.info}")
    def get(Location,attribute_name):
        if attribute_name == "NAME":
            return Location.name
        elif attribute_name == "INFO":
            return Location.info
        elif attribute_name == "VISITED_STATUS":
            return Location.been_visited
        elif attribute_name == "TEXT":
            return Location.text_list
    def set(Location,attribute_name,attribute_value):
        if attribute_name == "NAME":
            Location.name = attribute_value
        elif attribute_name == "INFO":
            Location.info = attribute_value
        elif attribute_name == "VISITED_STATUS":
            Location.been_visited = attribute_value
        elif attribute_name == "TEXT":
            Location.text_list = attribute_value
