from general import *
from Location_Data import Location_Dict
class Location:
    def Script_Runner(Location): # To be updated to run its own script
        for text in Location.text_list:
            Find_Execute_Command(Location.name,text)
    def __init__(Location,name,info,text_list=""): # Constructor
        Location.name = name
        Location.info = info
        Location.text_list = text_list
        Location.been_visited = False
    def __str__(Location): #String Representation
        str = Location.info
        if Location.been_visited:
            str =f"You are at {Location.name} Location Info: \n{Location.info}"
        return str
    def attribute(Location,type,attribute_name,new_val=""): #Returns or sets location_attributes
        attr = []
        if attribute_name == "NAME":
            attr[0] = Location.name
        elif attribute_name == "INFO":
            attr[0] = Location.info
        elif attribute_name == "VISITED_STATUS":
            attr[0] = Location.been_visited
        elif attribute_name == "TEXT":
            attr[0] = Location.text_list
        if type == "GET":
            return attr[0]
        elif type == "SET":
            attr[0] == new_val

