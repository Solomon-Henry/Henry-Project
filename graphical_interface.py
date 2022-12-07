from graphics import *
from color_schema import color_schema
from scene_data import scene_data
# To do

# To set up and implement entry type to input name and possibly other settings
# To set up and implement dialogue images and text box
# Integrate with main code, refactoring the main code to use the graphical interface
class Graphical_Interface:
    def __init__(GUI,name,width,height): # Declares graphical interface
        GUI.win = GraphWin(name,width,height)
        GUI.win.setCoords(0,0,width,height)
        GUI.current_action = "SETUP"
        GUI.current_scene_id = 0
        GUI.continue_status = True
    def graphic_action(GUI,type,scene_id): # Draws or undraws graphical objects from some scene
        current_scene_data = scene_data[scene_id]
        if type == "DRAW":
            for graphical_object_index in range(len(current_scene_data)): #Hotfix to not use the last default value
                graphical_object_data = current_scene_data[graphical_object_index]
                GUI.type_action(graphical_object_data,"DRAW")
        elif type == "UNDRAW":
            for graphical_object_index in range(len(current_scene_data)): #Hotfix to not use the last default value
                graphical_object_data = current_scene_data[graphical_object_index]
                GUI.type_action(graphical_object_data,"UNDRAW")
    def type_action(GUI,data,action): # Sets up or deletes graphical objects according to their type
        type = data.get("type")
        if type == "Button":
            graphical_object = data.get("object")
            if action == "DRAW":
                graphical_object.setFill(data.get("fill"))
                graphical_object.setOutline(data.get("outline"))
                graphical_object.draw(GUI.win)
            elif action == "UNDRAW":
                graphical_object.undraw()
        elif type == "Background":
            background_color = data.get("background_color")
            GUI.win.setBackground(background_color)
        elif type == "User_Input":
            if action == "DRAW":
                pass
            elif action == "UNDRAW":
                pass

            pass
        elif type == "Dialogue_Text":
            if action == "DRAW":
                pass
            elif action == "UNDRAW":
                pass
            pass
        elif type == "Dialogue_Image":
            if action == "DRAW":
                pass
            elif action == "UNDRAW":
                pass
            pass
        pass
    def unload_scene(GUI): # Unloads previously current scene
        GUI.graphic_action("UNDRAW",GUI.current_scene_id)
    def load_scene(GUI,id): # Loads current scene
        GUI.unload_scene()
        GUI.current_scene_id = id
        GUI.graphic_action("DRAW",GUI.current_scene_id)          
    def graphical_loop(GUI): # Game loop in charge of graphics
        while GUI.continue_status:
            GUI.action_runner(GUI.current_action)
            if not GUI.continue_status:
                break
            GUI.click_checker() 
        GUI.close_window()
    def action_runner(GUI,action): # Runs an action which is to be determined by which object the user clicked on
        if action.find("SETUP") != -1:
            GUI.load_scene(0)
        elif action.find("LOAD_SCENE") != -1:
            scene_id = int(action[-1])
            GUI.load_scene(scene_id)
        elif action.find("END_GAME") != -1:
            GUI.continue_status = False
        elif action.find("Dialogue_Cont") != -1: # To be functional when implementing dialogue
            next_dialogue = int(action[-1]) 
            pass
        elif action.find("NULL"):
            pass
    def click_checker(GUI): # To find out which object the user clicked on and buffer an action for action_runner
        mouse_coords = GUI.win.getMouse()
        if mouse_coords == None:
            GUI.current_action = "END_GAME"
        else:
            for obj in range(len(scene_data[GUI.current_scene_id])-1,-1,-1): # Iterates through the graphical objects backwards so that the background isn't drawn above the other graphical objects
                current_data = scene_data[GUI.current_scene_id][obj]
                bounds = current_data.get("object")
                if GUI.is_clicked(mouse_coords,bounds):
                    GUI.current_action = current_data.get("action")
                    break      
    def is_clicked(GUI,mouse_point,bounding_box): # To see if the user clicked within the bounding box of a graphical object
        if mouse_point.getX() >= bounding_box.getP1().getX() and mouse_point.getX() <= bounding_box.getP2().getX():
            if mouse_point.getY() >= bounding_box.getP1().getY() and mouse_point.getY() <= bounding_box.getP2().getY():
                return True
        return False
    def close_window(GUI): # Closes the window
        GUI.win.close()