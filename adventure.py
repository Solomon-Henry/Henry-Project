# New Reworked Version for Project 3. 

from Location_Data import Location_Dict

Quit_Status:bool = False
Death_Status:bool = False
Progress:int = 0
Name:str = ""
Score:int = 0


def min_max(min,max,val):
    ans = val
    if val < min:
        ans = min
    elif val > max:
        ans = max
    return ans
def Get_map_coord(val):
    coords = [None,None]
    str = Location_Dict[val]["Name"]
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if Map[i][j] == str:
                coords[0] = i
                coords[1] = j
                break
    return coords

Map = [
   ["OOB","Oasis","Turbine","Energy Deposit"],
   ["OOB","Estates","Hammond Labs","Grow Towers"],
   ["Hydroponis","Phase Driver","Solar Array","Orbital Cannon"],
   ["OOB","OOB","Bonsai Palace","Bonsai Palace","Icarus"],
   ["OOB","OOB","OOB","OOB"]
]
User_Commands = ["EXAMINE","HELP","QUIT"]
Text_Commands = ["TEXT","PROMPT","SET","CHOICE"]

class Stop:
    def __init__(Stop,LocationID):
        
        Stop.Id = LocationID
        Stop.Location = Location_Dict[Stop.Id]
        Stop.Name = Stop.Location["Name"]
        Stop.Location_Info = Stop.Location["Examine"]
        Stop.Map_Coordinates = Get_map_coord(Stop.Id)
        Stop.Text_List = Stop.Location["Text_List"]
    def Text_Command(Stop,str):
        #Finds text command in between two of the following character |
        global Name,Death_Status
        Text = str
        command = str[str.index("|")+1:str[str.index("|")+1:].index("|")+str.index("|")+1]
        Name_Replace_Index = str.find("|USERNAME|")
        if Name_Replace_Index != -1:
            Text = Text[:Name_Replace_Index] + Name + Text[Name_Replace_Index+len("|USERNAME|"):]
        if command == Text_Commands[0]:
            #Text
            print_str = Text[len(command)+2:]
            print(print_str)
        elif command == Text_Commands[1]:
            #Prompt
            prompt_str = Text[len(command)+2:]
            user_response = input(prompt_str+" ")
            Stop.User_Command(user_response)
        elif command == Text_Commands[2]:
            #Set
            set_str = Text[len(command)+2:]
            Name = input(set_str+" ")
        elif command == Text_Commands[3]:
            Correct_Continue = Text[len(command)+2:]
            Correct_Answer = Location_Dict[int(Stop.Id)+1]["Name"] 
            N = Map[min_max(0,4,Stop.Map_Coordinates[0]-1)][Stop.Map_Coordinates[1]]
            S = Map[min_max(0,4,Stop.Map_Coordinates[0]+1)][Stop.Map_Coordinates[1]]
            W = Map[Stop.Map_Coordinates[0]][min_max(0,3,Stop.Map_Coordinates[1]-1)]
            E = Map[Stop.Map_Coordinates[0]][min_max(0,3,Stop.Map_Coordinates[1]+1)]
            Directions = [N,S,W,E]
            Options = []
            Location_Dict_Indexes = []
            Printed_Options = []
            for c in Directions:
                if not (c == "OOB" or c == Map[Stop.Map_Coordinates[0]][Stop.Map_Coordinates[1]]):
                    Options.append(c)
            for j in Options:
                for i in Location_Dict:
                    if Location_Dict[i]["Name"] == j:
                        Location_Dict_Indexes.append(i)
            for k in Location_Dict_Indexes:
                Printed_Options.append([Location_Dict[k]["Name"],Location_Dict[k]["Examine"]])
            options_str = "\n"
            for m in Printed_Options:
                options_str = "\n" + m[0] + ": " + m[1]
                print(options_str) 
            user_choice = "\nChoose one of the options above, i.e the corresponding name: "
            def check():
                str  = input(user_choice)
                Surrounding_Locations = []
                for name in Printed_Options:
                    Surrounding_Locations.append(name[0])
                is_option = True if str in Surrounding_Locations else False
                if str == "" or not is_option:
                    print("\nNo rushing! Please type in one of the options")
                    str = check()    
                return str
            user_response = check()
            if user_response == Correct_Answer:
                print("\nGreat choice. You continue with your life.")
                input(Correct_Continue)
            else: 
                input("\nBad decision, you will now be dead\nPress enter to continue ")
                Death_Status =  True    
             
    def User_Command(Stop,user_str):
        global Quit_Status
        for i in User_Commands:
            #Functionality for user_command to be set up
            if user_str.find(i) != -1:
                if i == "EXAMINE":
                    print("Examine Info: ")
                    print(Stop.Location_Info)
                    input("\nPress Enter To Return To Story")
                    pass
                elif i == "HELP":
                    print("Help info: ")
                    print("\nValid Commands:\n\nEXAMINE: Find info on current location\nHELP: Display all valid commands\nQUIT: End game abruptly\n")
                    input("Press enter To Return To Story")
                elif i == "QUIT":
                    input("\nYou have quit the game.\nPress enter to continue to the end of the game :(")
                    Quit_Status = True
                    pass
                pass
        pass
    def Display_Progress(Stop):
        global Score,Progress
        Story_Progress:int
        if str(Stop.Id).isnumeric():
            Progress = Progress + 1
            Story_Progress = (Progress/10) * 100
            print(f"\nStory Progress: {Story_Progress}%\nTotal Score: {Score} points")
    def Story_Sequence(Stop): # To be completed
        global Score
        if (str(Stop.Id).isnumeric()) and (int(Stop.Id) >= 1 and int(Stop.Id)<=10) and (Stop.Location["Was_Visited"] == False):
            Score = Score + 10
            Stop.Location["Was_Visited"] == True
        for i in Stop.Text_List:
            if Quit_Status or Death_Status:
                break
            print("****************************************")
            Stop.Text_Command(i)
            print("****************************************")
            if Stop.Text_List.index(i) == len(Stop.Text_List)-1:
                Stop.Display_Progress()

Stop_1:Stop = Stop(1)
Stop_2:Stop = Stop(2)
Stop_3:Stop = Stop(3)
Stop_4:Stop = Stop(4)
Stop_5:Stop = Stop(5)
Stop_6:Stop = Stop(6)
Stop_7:Stop = Stop(7)
Stop_8:Stop = Stop(8)
Stop_9:Stop = Stop(9)
Stop_10:Stop = Stop(10)
Stop_Start:Stop = Stop(0)
Stop_Quit:Stop = Stop(13)
Stop_Death:Stop = Stop(12)
Stop_Final:Stop = Stop(11)
Stop_List = [Stop_Start,Stop_1,Stop_2,Stop_3,Stop_4,Stop_5,Stop_6,Stop_7,Stop_8,Stop_9,Stop_10,Stop_Quit,Stop_Death,Stop_Final]

## Game_Loop (Done)
def Game_Loop():
    for Places in Stop_List:
        if (Stop_List.index(Places) >= len(Stop_List)-3):
            break
        elif Quit_Status:
            Stop_Quit.Story_Sequence()
            break
        elif Death_Status:
            Stop_Death.Story_Sequence()
            break
        Places.Story_Sequence()
    Restart_Prompt()

def Restart_Prompt():
    global Quit_Status,Death_Status,Progress,Name,Score
    if (not Quit_Status) and (not Death_Status) :
        ans = input("\nGreat job on finishing the game!\nYou can restart by typing 'yes' or quit by pressing enter here: ")
    else:
        ans = input("You can choose to restart by typing 'yes' or quit by pressing enter: ")
    if ans == "yes":
        Quit_Status = False
        Death_Status = False
        Progress = 0
        Name = ""
        Score = 0
        Game_Loop()
    else:
        Stop_Final.Story_Sequence()

def main():
    Game_Loop()
    
main()