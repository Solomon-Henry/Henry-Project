# To-Do add functionality to print out on text_lists and prompt user with choices
class Location:

    def __init__(Location,name,info,text_list=""):
        Location.name = name
        Location.info = info
        Location.text_list = text_list
        Location.been_visited = False
    def __str__(Location):
        if Location.been_visited:
            print(f"You are at {Location.name}") 
        print(f"Location info:\n{Location.info}")
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
