# New Reworked Version for Project 3. (Unfinished Sketch)
# To Be Done
# Bring the missing variables from the old_adventure file and reformat them when necessary
# Use previously stated variables for the correct initialization of the Stop instances
# Properly initialize Location_List, Map, and any variables needed for the proper and 
#Complete the functions Divider, Command_Index, and implement them in the Story Sequence method.
# Complete the Stop class' methods: Story_Sequence and Setter. 
# Fix the function Display_Progress 

## Variables 
# (Missing many necessary variables, so the stop class instances are filled with dummy data)
# (Bring the needed variables from the old_adventure file and reformat them if necessary)



Quit_Status:bool = False
Name:str = ""


# Text related variables
# Key: (TEXT: regular text) (PROMPT: prompt for user to continue or make a choice) (PATH: To create alt path)
# Make a list for alt_lists




# Location_List (List of all locations with each index referring to the name of a location as a string)
Location_List = [
    None,
    "Courtroom",
    "Dropship",
    "Hammond Labs",
    "Estates",
    "Secret Trapdoor",
    "Phase Driver",
    "Solar Array", 
    "Bonsai Palace",
    "Champion's Palace",
    "Prison Dropship",
    None,
]
# Location_List_Info (A dictionary of all the locations along with their corresponding in the game) 
# (Value stored as stop num and info)
# (The original travelable locations are numbered from 1-9, all other locations will be numbered outside of range) 
# To be completed and filled with meaningful values
Location_List_Info = {
    "Courtroom" : [[0,2],"Courts bois"]

}
# Map (A matrix where all the in-game locations are placed as they would be, representing travel destinations)
# To be completed and filled with meaningful values
Map = [
   ["OOB","Oasis","Turbine","Energy Deposit"],
   ["OOB","Estates","Hammond Labs","Grow Towers"],
   ["Hydroponis","Phase Driver","Solar Array","Orbital Cannon"],
   ["OOB","OOB","Bonsai Palaca","Icarus"],
   ["OOB","OOB","OOB","OOB"]
]

# User Commands(All viable commands which user can use whennever they aren't at a fixed or final continue, with some exceptions)
# The first 3 commands can be paired with a cardinal direction or 'CL' to either move the user there or look/examine the area
# Typing in Look or Examine will print out corresponding info for current and all nearby locations
User_Commands = ["GO","LOOK","EXAMINE","HELP","QUIT"]
# Text Commands (For Story_Sequence method to know if to make string a regular text, prompt, variable, make new path, return to old path, or dead end )
Text_Commands = ["TEXT","PROMPT","SET","PATH","RETURN","DEATH"]
## Stops
# Note (User_Script is now Fixed_Cont)
# Alternate paths are only in mini_stops
# Final Continues are transitions between stops
# Methods: Story_Sequence (Maybe automatically uses asterisk separator)(Can use alternate paths)(Can handle commands especially QUIT)
class Stop:
    def __init__(Stop,LocationID,TextList):
        Stop.Location = Location_List[LocationID]
        Stop.Location_Info = Location_List_Info[Stop.Location][1]
        Stop.Map_Coordinates = Location_List_Info[Stop.Location][0]
        Stop.Text_List = TextList
        Stop.Skips = 0
        Stop.Final_Continue = TextList[-1]
    def Text_Divider(Stop):
        pass
    def Text_Command(Stop,str):
        #Finds text command in between two of the following character |
        command = str[str.index("|")+1:str[str.index("|")+1:].index("|")+str.index("|")+1]
        if command == Text_Commands[0]:
            #Text; Functional
            print_str = str[len(command)+2:]
            print(print_str)
            pass
        elif command == Text_Commands[1]:
            #Prompt: Not Finished, set up user_command function
            prompt_str = str[len(command)+2:]
            user_response = input(prompt_str)
            Stop.User_Command(user_response)
            Stop
            pass
        elif command[:-1] == Text_Commands[2]:
            #Set: Not Finished
            set_str = str[len(command)+2:]
            set = input(set_str)
            Name = set
            # Change corresponding variables that need users name
            pass
        elif command[:-1] == Text_Commands[3]:
            #Path, Will call iteration to iterate through alt path and update Stop.Skips so that when returning to
            # original path, the skipped mini stops will actually be skipped
            # Not Finished
            pass
        elif command[:-1] == Text_Commands[4]:
            #Return, bring user back to original path
            # Not Finished
            pass
        elif command == Text_Commands[5]:
            #Death, Not Finished
            pass
        pass
    def User_Command(Stop,user_str):
        for i in User_Commands:
            #Functionality for user_command to be set up
            if user_str.find(i) != -1:
                if i == "GO":
                    pass
                elif i == "LOOK":
                    pass
                elif i == "EXAMINE":
                    pass
                elif i == "HELP":
                    pass
                elif i == "QUIT":
                    pass
                pass
        pass
    def Display_Progress(Stop):
        pass
    def Iterate(arr):
        for i in range(len(arr)):
            Stop.Text_Command(i)
            Stop.Skips = Stop.Skips + 1
            pass
        pass
    def Story_Sequence(Stop): # To be completed
        # Iterate through array
        # Act based on text command keyword in string
        # Be able to use text, prompts and setters
        # How to get deaths to work
        for i in Stop.Text_List:
            if Stop.Skips != 0:
                Stop.Skips = Stop.Skips - 1
                continue
            Stop.Text_Command(i)
            if Stop.Text_List.index(i) == len(Stop.Text_List)-1:
                Stop.Display_Progress()
        pass
c = ["|TEXT|\naaaa"]
Stop_Test:Stop = Stop(1,c)
Stop_Test.Story_Sequence()
# Individual instances of Stops to be defined properly, shown values are simply dummy ones for the sole purpose of testing

Stop_1:Stop
Stop_2:Stop
Stop_3:Stop
Stop_4:Stop 
Stop_5:Stop
Stop_6:Stop 
Stop_7:Stop 
Stop_8:Stop 
Stop_9:Stop
Stop_10:Stop 
Stop_Start:Stop 
Stop_Quit:Stop 
Stop_Final:Stop 
#Stop_List = [Stop_Start,Stop_1,Stop_2,Stop_3,Stop_4,Stop_5,Stop_6,Stop_7,Stop_8,Stop_9,Stop_10,Stop_Quit,Stop_Final]
Stop_List = []



## Game_Loop (Done)
# iterate through the Stops classes (Numericals only) (Change Stop A to numerical)
# break if Quit_Status is true
# use Story_Sequence method for each Stop class in Stop_list
# Display Progress 
# Print Final_Continue attribute as an input
def Game_Loop():
    for Places in Stop_List:
        if (Stop_List.index(Places) >= len(Stop_List)-2):
            break
        elif Quit_Status:
            Stop_Quit.Story_Sequence()
            break
        Places.Story_Sequence()
    Restart_Prompt()

## Restart_Prompt (Done)
# prompt user to restart
# if yes then call another Game_Loop function
# else use Story_Sequence method for Stop_Final
def Restart_Prompt():
    ans = input("You can choose to restart by typing 'yes' or quit by pressing enter: ")
    if ans == "yes":
        Game_Loop()
    else:
        Stop_Final.Story_Sequence()


## Main (Done)
# Calls and initiates the Game_loop
# 
def main():
    Game_Loop()
    
#main()