# Game related string text 
Game_Title = "\nGame_Title Test "
Game_Description = "\nGame_Description Test"
Stop_A_Text_List = [Game_Title, Game_Description]
Game_Despedida = "\n Game Despedida Test"
Stop_F_Text_List = [Game_Despedida]
# List of places and text sections
Stop_0 = "Stop 0"
Stop_0_Text_0 = "\nAw Yeah"
Stop_0_Text_List = [Stop_0_Text_0]
Stop_1 = "Stop 1"
Stop_1_Text_0 = ""
Stop_1_Text_List = [Stop_1_Text_0]
Stop_2 = "Stop 2"
Stop_2_Text_0 = ""
Stop_2_Text_List = [Stop_2_Text_0]
Stop_3 = "Stop 3"
Stop_3_Text_0 = ""
Stop_3_Text_List = [Stop_3_Text_0]
Stop_4 = "Stop 4"
Stop_4_Text_0 = ""
Stop_4_Text_List = [Stop_4_Text_0]
Stop_5 = "Stop 5"
Stop_5_Text_0 = ""
Stop_5_Text_List = [Stop_5_Text_0]
Stop_6 = "Stop 6"
Stop_6_Text_0 = ""
Stop_6_Text_List = [Stop_6_Text_0]
Stop_7 = "Stop 7"
Stop_7_Text_0 = ""
Stop_7_Text_List = [Stop_7_Text_0]
Stop_8 = "Stop 8"
Stop_8_Text_0 = "hmm"
Stop_8_Text_List = [Stop_8_Text_0]
Stop_9 = "Stop 9"
Stop_9_Text_0 = ""
Stop_9_Text_List = [Stop_9_Text_0]

Location_List = [Stop_0,Stop_1,Stop_2,Stop_3,Stop_4,Stop_5,Stop_6,Stop_7,Stop_8,Stop_9]
Text_List_List = [Stop_A_Text_List,Stop_0_Text_List,Stop_1_Text_List,Stop_2_Text_List,Stop_3_Text_List,Stop_4_Text_List,Stop_5_Text_List,Stop_6_Text_List,Stop_7_Text_List,Stop_8_Text_List,Stop_9_Text_List,Stop_F_Text_List]

# Variables to keep track of how far the user is 
Stop_Marker = "a"
Stop_Marker_List = ["a",0,1,2,3,4,5,6,7,8,9,"f"]

# Defining Functions
def Display_Progress():
    current_stop:int
    story_percentage:int
    current_location:str
    number_suffix:str
    if not Stop_Marker == "f" and not Stop_Marker == "a":
        story_percentage = (Stop_Marker+1)  * 10
        print(f"{Stop_Marker}")
        print(Location_List[Stop_Marker])
        current_location = Location_List[(Stop_Marker)] 
        if Stop_Marker+1  == 1:
            number_suffix = "st"
        elif Stop_Marker+1  == 2: 
            number_suffix = "nd"
        else:
            number_suffix = "th"
        print(f"\nCurrent Game Location is {current_location}, The Game's {Stop_Marker+1}{number_suffix} location \nStory completion is at {story_percentage}%\n")
    

def Asterisk_separator(): 
    str = ""
    for i in range(70):
        str = str + "*"
    print(f"\n{str}")    

def Find_Stop_Marker():
    if Stop_Marker == "a":
        return 0
    elif Stop_Marker == "f":
        return len(Stop_Marker_List) - 1
    else:
        return Stop_Marker + 1 

def Script_Runner(n):
    msg = ""
    cnt = 0
    for i in Text_List_List[n]:
        if cnt == len(Text_List_List[n])-1:
            msg =  msg + Text_List_List[n][cnt] # + "\n"
        else: 
            msg = msg + Text_List_List[n][cnt]
        cnt = cnt + 1
    print(f"{msg}")


def Auto_Proceed():
    global Stop_Marker
    Asterisk_separator()
    Script_Runner(Find_Stop_Marker())
    Stop_Marker = Stop_Marker_List[Find_Stop_Marker()+1]

def GoTo(loc:int):
    global Stop_Marker
    Stop_Marker = Stop_Marker_List[loc]
    Auto_Proceed()

def User_Proceed():
    global Stop_Marker
    user_prompt = input("Press Enter to proceed")
    if user_prompt or not user_prompt:
        Asterisk_separator()
        Script_Runner(Find_Stop_Marker())
        Display_Progress()
        Stop_Marker = Stop_Marker_List[Find_Stop_Marker()+1]
        
def Restart():
    global Game_Loop_Count
    ans = input("You can choose to restart by typing 'y' and pressing enter: ")
    if ans == "y":
        GoTo(0)
        Game_Loop_Count = 0
        Game_Loop()
    else:
        #GoTo(-1)
        Script_Runner(-1)
Game_Loop_Count = 0
def Game_Loop():
    global Game_Loop_Count
    for i in Text_List_List:
        if not Game_Loop_Count == len(Text_List_List)-2:
            User_Proceed()
            Game_Loop_Count = Game_Loop_Count + 1
        else: 
            break
    Restart()


def main():
    GoTo(0)
    Game_Loop()

main()