from general_functions import*
from location import*
from Location_Data import*

class World:
    def location_intialization(World):
        Main_Story_Sequence = []
        Alt_Story_Sequence = []
        for i in range(len(Location_Dict)):    
            Main_Story_Sequence[i] = Location(Location_Dict[i].get("Name"),Location_Dict[i].get("Text_List"),Location_Dict[i].get("Examine"))
        return Main_Story_Sequence
        pass
    def id_to_map_coords(World):
        search_value = Location_Dict[World.current_location_id].get("Name")
        map_coords = []
        break_status = False
        for i in World.map:
            for j in World.map[i]:
                if World.map[i][j] == search_value:
                    map_coords = i, j
                    break_status = True
                    break
            if break_status:
                break
        return map_coords
    def name_to_id(World,name):
        id:int
        keys = list(Location_Dict.keys())
        for key in keys:
            if Location_Dict[key].get("Name") == name:
                return key
    def __init__(World):
        # Numerical values represent each locale, make a key using location_data 
        World.main_sequence = World.location_intialization() 
        World.current_location_id = 0
        World.map =[
                    ["OOB","Oasis","Turbine","Energy Deposit"],
                    ["OOB","Estates","Hammond Labs","Grow Towers"],
                    ["Hydroponis","Phase Driver","Solar Array","Orbital Cannon"],
                    ["OOB","OOB","Bonsai Palace","Bonsai Palace","Icarus"],
                    ["OOB","OOB","OOB","OOB"]
                    ]
    def update_location(World,jump="False"):
        if jump == "False":
            World.current_location_id += 1
        else:
            World.current_location_id = jump
    def get_location_name(World):
        return Location_Dict[World.current_location_id].get("Name")
    def get_surrounding_locations(World):
        #Return surrounding locations by id
        #North, South, West, East
        current_coords = World.id_to_map_coords(World.current_location_id)
        row = current_coords[0]
        col = current_coords[1]
        current_location = World.map[row][col]
        cardinal_directions = [[-1,0],[1,0],[0,-1],[0,1]]
        surrounding_locations_names = []
        for direction in cardinal_directions:
            row_offset = direction[0]
            col_offset = direction[1]
            offset_location = World.map[min_max(row+row_offset)][min_max(col+col_offset)]
            if not (offset_location == current_location) or not (offset_location == "OOB"):
                surrounding_locations_names.append(offset_location)
        surrounding_locations_id = map(World.name_to_id,surrounding_locations_names)
        return surrounding_locations_id
