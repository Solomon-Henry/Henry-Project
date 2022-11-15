class Locale:

    def __init__(Locale,name,info,text_list):
        Locale.name = name
        Locale.info = info
        Locale.text_list = text_list
        Locale.been_visited = False
    def __str__(Locale):
        if Locale.been_visited:
            print(f"You are at {Locale.name}") 
        print(f"Location info:\n{Locale.info}")
    def get(Locale,attribute_name):
        if attribute_name == "NAME":
            return Locale.name
        elif attribute_name == "INFO":
            return Locale.info
        elif attribute_name == "VISITED_STATUS":
            return Locale.been_visited
        elif attribute_name == "TEXT":
            return Locale.text_list
    def set(Locale,attribute_name,attribute_value):
        if attribute_name == "NAME":
            Locale.name = attribute_value
        elif attribute_name == "INFO":
            Locale.info = attribute_value
        elif attribute_name == "VISITED_STATUS":
            Locale.been_visited = attribute_value
        elif attribute_name == "TEXT":
            Locale.text_list = attribute_value
