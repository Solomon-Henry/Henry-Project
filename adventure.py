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

# Location_List (A dictionary of all the locations along with their corresponding in the game) (Value stored as stop num and info)
# To be completed and filled with meaningful values
Location_List = {
    "Courtroom" : [0,"A place where courts happen"]
}

# Map (A matrix where all the in-game locations are placed as they would be, representing travel destinations)
# To be completed and filled with meaningful values
Map = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Command List (All viable commands which user can use whennever they aren't at a fixed or final continue, with some exceptions)
# The first 3 commands can be paired with a cardinal direction to either move the user there or look/examine the area
Commands = ["GO","LOOK","EXAMINE","HELP","QUIT"]
## Stops
# Note (User_Script is now Fixed_Cont)
# Alternate paths are only in mini_stops
# Attributes: Location_Text, Location_Info, Map_Coordinates, Text_List, Fixed_Continue, Final_Continue
# Fixed Continues are mini stop transitions where user has no choice except do the suggested option or examine the current or nearby areas
# Final Continues are transitions between 
# Methods: Story_Sequence (Maybe automatically uses asterisk separator)(Can use alternate paths)(Can handle commands especially QUIT)
# Methods: Setter (Only to be used for Stop A) (Initializes the name variable and places it in a predefined list of strings)

class Stop:
    def __init__(Stop,LocationText,MapCoord,TextList,FixedCont):
        Stop.Location_Text = LocationText
        Stop.Location_Info = Location_List[LocationText][1]
        Stop.Location_Number = Location_List[LocationText][0]
        Stop.Map_Coordinates = MapCoord
        Stop.Text_List = TextList
        Stop.Fixed_Continue = FixedCont
        Stop.Final_Continue = FixedCont[-1]
    def Story_Sequence(Stop): # To be completed
        print(Stop.Location_Info)
        print(f"Stop number {Stop.Location_Number}")
        pass
    def Setter(Stop): # To be completed
        pass

# Individual instances of Stops to be defined properly, shown values are simply dummy ones for the sole purpose of testing
Stop_0:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_1:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_2:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_3:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_4:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_5:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_6:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_7:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_8:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_9:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_10:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_Quit:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_Final:Stop = Stop("Courtroom",[0,1],["Line 1","Line 2"],"Cont")
Stop_List = [Stop_0,Stop_1,Stop_2,Stop_3,Stop_4,Stop_5,Stop_6,Stop_7,Stop_8,Stop_9,Stop_10,Stop_Quit,Stop_Final]

# Command_Index (To find out if user input contains a command and any cardinal directions if required)
# To be completed
def Command_Index(val):
    pass

# Divider (Separates text using newlines and asterisks
# To be completed
def Divider():
    pass

## Display_Progress (To be fixed)
def Display_Progress(Location,Stop_Number,Mini_Stop_Percent=100):
    story_len = len(Location_List)
    Additional_Percentage = (Mini_Stop_Percent/100)
    progress = (((Stop_Number)/story_len) + (Additional_Percentage*(1/story_len)))*100
    print(f"\nCurrent location is {Location}\nStory completion is at {progress}")
  
    

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
        Transition = input(Places.Final_Continue)    
        Display_Progress(Places.Location_Text,Places.Location_Number)
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
    
main()