from Text_Data import*
Game_Map = [
        ["OOB","Oasis","Turbine","Energy Deposit"],
        ["OOB","Estates","Hammond Labs","Grow Towers"],
        ["Hydroponis","Phase Driver","Solar Array","Orbital Cannon"],
        ["OOB","OOB","Bonsai Palace","Bonsai Palace","Icarus"],
        ["OOB","OOB","OOB","OOB"]
        ]
Location_Dict = {
    0 : {
        "Name" : "",
        "Text_List" : Stop_A_Text_List,
        "Examine" : ""
    },
    13 : {
        "Name" : "",
        "Text_List" : Stop_Quit_Text_List,
        "Examine" : ""
    },
    12 : {
        "Name" : "",
        "Text_List" : Stop_Death_Text_List,
        "Examine" : ""
    },
    11 : {
        "Name" : "",
        "Text_List" : Stop_F_Text_List,
        "Examine" : ""
    },
    1 : {
        "Name" : "Courtroom",
        "Text_List" : Stop_0_Text_List,
        "Examine" : "\nYou're in a courtroom, attesting for your crimes",
        "Was_Visited" : False
    },
    2 : {
        "Name" : "Dropship",
        "Text_List" : Stop_1_Text_List,
        "Examine" : "\nYou're now in a flying dropship, somehwere above the floating city of Olympus",
        "Was_Visited" : False
    },
    3 : {
        "Name" : "Hammond Labs",
        "Text_List" : Stop_2_Text_List,
        "Examine" : "\nYou're at Hammond Labs with an angry enemy squad with guns",
        "Was_Visited" : False
    },
    4 : {
        "Name" : "Estates",
        "Text_List" : Stop_3_Text_List,
        "Examine" : "\nA place with fancy houses for fancy people",
        "Was_Visited" : False
    },
    5 : {
        "Name" : "Secret Trapdoor",
        "Text_List" : Stop_4_Text_List,
        "Examine" : "\nYou're in a Secret Trapdoor, maybe you should get out somehow before danger finds its way to you again",
        "Was_Visited" : False
    },
    6 : {
        "Name" : "Phase Driver",
        "Text_List" : Stop_5_Text_List,
        "Examine" : "\nNothing special here, except the two teams killing each other, nothing out of the ordinary in the Apex games",
        "Was_Visited" : False
    },
    7 : {
        "Name" : "Solar Array",
        "Text_List" : Stop_6_Text_List,
        "Examine" : "\nAs the name suggests, an area solely devoted to having solar panels in arrays",
        "Was_Visited" : False
    },
    8 : {
        "Name" : "Bonsai Palace",
        "Text_List" : Stop_7_Text_List,
        "Examine" : "\nA palace with so many beautiful artworks. They surely wouldn't miss a few dozen of them, right?",
        "Was_Visited" : False
    },
    9 : {
        "Name" : "Champion's Podium",
        "Text_List" : Stop_8_Text_List,
        "Examine" : "\nThis is where champions are found, like you",
        "Was_Visited" : False
    },
    10 : {
        "Name" : "Prison Dropship",
        "Text_List" : Stop_9_Text_List,
        "Examine" : "\nYou're now going back to jail in a Prison Dropship, you didn't forget you were a criminal right?",
        "Was_Visited" : False
    },
    14 : {
        "Name" : "Oasis",
        "Examine" : "A nice tourist trap with lots of places to relax, conveniently placed right at the edge of the map"
    },
    15 : {
        "Name" : "Turbine",
        "Examine" : "\nA place wih a giant turbine which keeps the floating city of Olympus afloat"
    },
    16 : {
        "Name" : "Energy Deposit",
        "Examine" : "\nJust Olympus's main power grid. May be important later"
    },
    17 : {
        "Name" : "Grow Towers",
        "Examine" : "\nA place where large spiraling towers are covered with greenery"
    },
    18 : {
        "Name" : "Hydroponis",
        "Examine" : "\nA small part of Olympus that is host to many plants, serving as their watering system"
    },
    19 : {
        "Name" : "Orbital Cannon",
        "Examine" : "\nOrbital Cannon. It's name speaks for itself"
    },
    20 : {
        "Name" : "Icarus",
        "Examine" : "\nA wrecked ship containing the deadlist virus in the the galaxy. Best not to go there"
    },
    21 : {
        "Name" : "OOB",
        "Examine" : "\nInaccessible Area"
    }
}

