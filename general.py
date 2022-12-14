from Location_Data import Location_Dict,Game_Map
player_list = []
location_list = []
min_max_values = (0,3)
User_Commands = ["EXAMINE","HELP","QUIT","SAVE","LOAD"]
Text_Commands = ["TEXT","PROMPT","SET","CHOICE","|USERNAME|"]
def get_surrounding_locations(id): #Returns numerical ids of surrounding locations
    current_coords = translate("ID",id,"MAP_COORD")
    row = current_coords[0]
    col = current_coords[1]
    current_location = Game_Map[row][col]
    cardinal_directions = [[-1,0],[1,0],[0,-1],[0,1]] #N,S,W,E
    surrounding_locations_names = []
    for direction in cardinal_directions:
        row_offset = direction[0]
        col_offset = direction[1]
        offset_location = Game_Map[min_max(row+row_offset)][min_max(col+col_offset)]
        if not (offset_location == current_location) or not (offset_location == "OOB"):
            surrounding_locations_names.append(offset_location)
    surrounding_locations_id = []
    for name in surrounding_locations_names:
        surrounding_locations_id.append(translate("NAME",name,"ID"))
    return surrounding_locations_id
def map_search(name):#Returns coordinates of location on map by its name
    break_status = False
    coords = [None,None]
    for row in range(len(Game_Map)):
        for col in range(len(Game_Map[row])):
            if Game_Map[row][col] == name:
                coords[0] = row
                coords[1] = col
                break_status = True
                break
        if break_status:
            break
    return coords
def translate(var_type,var,new_type):#To give the numerical id of a location from its name, or vice-versa, or even from its map_coords
    search_term = var
    return_val = None
    if var_type == "MAP_COORD":
        search_term = Game_Map[var[0]][var[1]]
        var_type = "NAME"
    for key in range(len(Location_Dict)):
        if var_type == "NAME":
            if Location_Dict[key].get("Name") == search_term:
                if new_type == "ID":
                    return_val = key
                elif new_type == "MAP_COORD":
                    return_val = map_search(search_term)
                    
                break
        elif var_type == "ID":
            if key == search_term:
                if new_type == "NAME":
                    return_val = Location_Dict[key].get("Name")
                elif new_type == "MAP_COORD":
                    loc_name = Location_Dict[key].get("Name")
                    return_val = map_search(loc_name)
    return return_val

    """""
    Id
    Map coords
    Name
    """""
    pass
def min_max(val):
    min, max = min_max_values
    ans = val
    if val < min:
        ans = min
    elif val > max:
        ans = max
    return ans
def Find_Execute_Command(loc_name,str): 
        retval = None
        print()
        location_id = translate("NAME",loc_name,"ID")
        current_location = location_list[location_id]
        command = str[str.index("|")+1:str[str.index("|")+1:].index("|")+str.index("|")+1]
        current_player = player_list[-1]
        Text = str
        Text = str[len(command)+2:]
        check_username = Text.find(Text_Commands[4])
        if check_username != -1:
            Text = Text[:check_username] + current_player.get_name() + Text[check_username+len(Text_Commands[4]):]
        if command == Text_Commands[0]:
            print(Text)
        elif command == Text_Commands[1]:
            user_input = input(Text+" ")
            retval = find_run_user_command(current_location,current_player,user_input)
        elif command == Text_Commands[2]:
            user_input = input(Text+" ")
            current_player.set_name(user_input)
        elif command == Text_Commands[3]:
            option_ids = get_surrounding_locations(location_id)
            options_text = []
            for id in option_ids:
                text = [None,None]
                text[0] = "\n"+Location_Dict[id].get("Name") + ":"
                text[1] = Location_Dict[id].get("Examine")
                options_text.append(text)
            for option in options_text:
                for str in option:
                    print(f"{str}")
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
            correct_response = Location_Dict[location_id+1].get("Name")
            def chances(rep):
                if rep == correct_response:
                    print("\nGreat choice. You continue with your life.")
                    input(Text)
                else:
                    input("\nBad decision, you have achieved the death ending\nPress enter to see continue: ")
                    current_player.set_status("DEATH")
                    retval = True
            chances(user_response)
        return retval
def find_run_user_command(loc_instance,player,str):
        retval = None
        if str == "":
            pass
        elif str.find(User_Commands[0]) != -1:
            print("Examine Info: ")
            print(loc_instance)
            input("\nPress Enter To Return To Story")
        elif str.find(User_Commands[1]) != -1:
            print("Help info: ")
            print("\nValid Commands:\n\nEXAMINE: Find info on current location\nHELP: Display all valid commands\nQUIT: End game abruptly\nnSAVE: Create a save file which you can nanme\nLOAD: Load in a pre-made save file")
            input("Press enter To Return To Story")
        elif str.find(User_Commands[2]) != -1:
            input("\nYou have quit the game.\nPress enter to continue to the end of the game :(")
            player.set_status("QUIT")
            retval = True
        elif str.find(User_Commands[3]) != -1:
            #Save
            save_data_action("WRITE")
        elif str.find(User_Commands[4]) != -1:
            #Load
            save_data_action("READ")
            retval = True
        else:
            pass
        return retval
def save_file_exists(name):
    try:
        file = open(name,"r")
        file.close()
        return True
    except:
        return False

def prompt(str):
    rep = input(str)
    return rep
def save_data_action(action,recur=False):
    if action == "WRITE":
        save_file_name = prompt("\nEnter name of new save file you wish to create: ") + ".txt"
        if not save_file_exists(save_file_name):
            save_file = open(save_file_name,"w")
            save_file.write(player_list[0].save_data)
            save_file.close()
            print(f"\nSave file {save_file_name} has been created.")
            input("\nPress Enter to continue")
        else:
            print("\nSave file with that name already exists.\nPlease enter a valid name")
            save_data_action("WRITE",True)
    elif action == "READ":
        save_file_name = prompt("\nEnter name of new save file you wish to load: ") + ".txt"
        if save_file_exists(save_file_name):
            save_file = open(save_file_name,"r")
            save_data = []
            for line in save_file:
                save_data.append(line)
            save_file.close()
            input(f"\nSave file {save_file_name} has been loaded.\nPress Enter to continue: ")
            player_list[0].set_status("LOAD",save_data)
        else:
            print("\nNo save file with that name exists.\nPlease enter a valid name")
            save_data_action("READ",True)
        pass
