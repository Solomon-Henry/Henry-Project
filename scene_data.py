from graphics import *
from color_schema import*
# Types:
# Background
# Button
# To set up
# User_Input
# Dialogue_Image
# Dialogue_TextBox
scene_data = { # Key: Scene number, id of objects
    0 : {
            0: {
                "type" : "Background",
                "object" : Rectangle(Point(0,0),Point(background[0],background[1])),
                "background_color" : color_schema["green"],
                "action" : "END_GAME"
            },
            1 : {
                "type" : "Button",
                "object" : Rectangle(Point(600,400),Point(800,700)),
                "fill": "orange",
                "outline": "pink",
                "action" : "LOAD_SCENE 0"
            }
        
    }
}
