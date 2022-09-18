# Game related string text 
Game_Title = "\nGame_Title Test "
Game_Description = "\nGame_Description Test"
Stop_A_Text_List = [Game_Title, Game_Description]
Game_Despedida = "\nGame Despedida Test"
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
Stop_8_Text_0 = ""
Stop_8_Text_List = [Stop_8_Text_0]
Stop_9 = "Stop 9"
Stop_9_Text_0 = ""
Stop_9_Text_List = [Stop_9_Text_0]

# Don't use prompt at the end of text list
User_Script_Prompt_List = [
     [["P"], ["a2 aw yeahhhhh"], ["a3"]],
     [[], [], []],
     [[], [], []],
     [[], [], []],
     [[], [], []],
     [[], [], []],
     [[], [], []],
     [[], [], []],
     [[], [], []],
     [[], [], []]
]
Continue_Prompt_List = [
    "Game Start Continue",
    "Stop 0 - 1",
    "Stop 1 - 2",
    "Stop 2 - 3",
    "Stop 3 - 4",
    "Stop 4 - 5",
    "Stop 5 - 6",
    "Stop 6 - 7",
    "Stop 7 - 8",
    "Stop 8 - 9" 
]
Location_List = [Stop_0,Stop_1,Stop_2,Stop_3,Stop_4,Stop_5,Stop_6,Stop_7,Stop_8,Stop_9]
Text_List_List = [Stop_A_Text_List,Stop_0_Text_List,Stop_1_Text_List,Stop_2_Text_List,Stop_3_Text_List,Stop_4_Text_List,Stop_5_Text_List,Stop_6_Text_List,Stop_7_Text_List,Stop_8_Text_List,Stop_9_Text_List,Stop_F_Text_List]

# Variables to keep track of how far the user is 
Stop_Marker = "a"
Stop_Marker_List = ["a",0,1,2,3,4,5,6,7,8,9,"f"]

# Defining Functions

# To show how far user is in story
def Display_Progress():
    story_percentage:int
    current_location:str
    number_suffix:str
    if not Stop_Marker == "f" and not Stop_Marker == "a":
        story_percentage = (Stop_Marker+1)  * 10
        current_location = Location_List[(Stop_Marker)] 
        if Stop_Marker+1  == 1:
            number_suffix = "st"
        elif Stop_Marker+1  == 2: 
            number_suffix = "nd"
        elif Stop_Marker+1 == 3:
            number_suffix = "rd"
        else:
            number_suffix = "th"
        Asterisk_separator(0,0)
        print(f"Current Game Location is {current_location}, The Game's {Stop_Marker+1}{number_suffix} location \nStory completion is at {story_percentage}%")
# To mark different sections using asterisks 
def Asterisk_separator(a=1,b=1, visible=True): 
    str = ""
    if visible:
        for i in range(70):
            str = str + "*"
        for i in range(a):
            str = "\n" + str
        for i in range(b):
            str = str + "\n"
    print(str) 
# To translate the Stop_Marker into its location in the Stop_Marker_List
def Find_Stop_Marker():
    if Stop_Marker == "a":
        return 0
    elif Stop_Marker == "f":
        return len(Stop_Marker_List) - 1
    else:
        return Stop_Marker + 1 
# To prompt the user with the correct in-text prompt upon being given its id
def User_Script_Prompt(i_d):
    i_d_c = int(i_d[0])
    i_d_r = int(i_d[1]) 
    prompt_str =  User_Script_Prompt_List[i_d_c][i_d_r][0]
    p = input(f"{prompt_str}")
# To print the correct series of texts from the Test_List_List, given its numerical id
def Script_Runner(n):
    msg = ""
    cnt = 0
    for i in Text_List_List[n]:
        if cnt == len(Text_List_List[n])-1:
            msg =  msg + Text_List_List[n][cnt] 
        elif Text_List_List[n][cnt][0:-2] == "PROMPT":
            User_Script_Prompt(Text_List_List[n][cnt][-2:len(Text_List_List[n][cnt])])
        else: 
            msg = msg + Text_List_List[n][cnt]
        cnt = cnt + 1
    print(f"{msg}")
# To go to a given Section autonomously
def Auto_Proceed():
    global Stop_Marker
    Asterisk_separator(0,0)
    Script_Runner(Find_Stop_Marker())
    Stop_Marker = Stop_Marker_List[Find_Stop_Marker()+1]
# To change stop Marker value accordingly and call auto_Proceed
def GoTo(loc:int):
    global Stop_Marker
    Stop_Marker = Stop_Marker_List[loc]
    Auto_Proceed()
# To call on correct prompt based on how far the user is in and print it
def User_Proceed():
    global Stop_Marker
    user_prompt_msg = Continue_Prompt_List[Find_Stop_Marker()-1]
    user_prompt = input(f"{user_prompt_msg}\n")
    if user_prompt or not user_prompt:
        Asterisk_separator(0,5)
        Script_Runner(Find_Stop_Marker())
        Display_Progress()
        Asterisk_separator(0,0)
        Stop_Marker = Stop_Marker_List[Find_Stop_Marker()+1]
# To give the user the option to repeat the game or go to ending
def Restart():
    global Game_Loop_Count
    ans = input("You can choose to restart by typing 'y' and pressing enter: ")
    if ans == "y":
        GoTo(0)
        Game_Loop_Count = 0
        Game_Loop()
    else:
        Asterisk_separator(0,0)
        Script_Runner(-1)
# To repeat the User_Proceed function, progressing the user into the game
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
# To start the game upon the program being run
def main():
    GoTo(0)
    Game_Loop()

main()