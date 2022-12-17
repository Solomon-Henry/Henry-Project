from general import min_max, location_list
from location import Location
from Location_Data import Location_Dict,Game_Map

class World:
    graphic_mode:bool = False
    def location_intialization(World): #Initializes list of locations
        for ID in range(len(Location_Dict)):    
            location_list.append(Location(Location_Dict[ID].get("Name"),Location_Dict[ID].get("Examine"),Location_Dict[ID].get("Text_List")))     
    def __init__(World): # Constructor
        World.location_intialization() 
        World.current_location_id = 0
        World.map = Game_Map
    def update_location(World,jump="False"):
        if jump == -1:
            World.current_location_id += 1
        else:
            World.current_location_id = jump
    def get_location(World,type): #Return some aspect of a locations or the location itself
        if type == "ID":
            return World.current_location_id
        elif type == "NAME":
            return Location_Dict[World.current_location_id].get("Name")
        elif type == "INSTANCE":
            return World.main_sequence[World.current_location_id]
    
