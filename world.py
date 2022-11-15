#To do what the path command does 
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
    def display_options(World):    
        # To be done, reliance on additional functionality in locale.py
        pass
