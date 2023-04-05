# Golan van der Bend 
# 2022-12-19
# Add buttons to BackdropNode
# Recreated the backdrop gizmo from 'Franklin Toussaint'. 

import nuke
import random


def addButtons():
    #############################################
    ###### Add buttons using python #############
    #############################################
    
    backdrop = nuke.thisNode()
    
    ### Pyton button scripts ###
    
    ## knob callbacks 
    ## -Slider for font size
    ## -Pulldown menu for font placement.
    def font_size_code():
        n = nuke.thisNode()
        k = nuke.thisKnob()
        l = nuke.thisKnob()
        if k.name() == "fontSize" : 
            n['note_font_size'].setValue(k.value())
        
        
        if k.name() == "fontPlacement":
            if k.value() == "left":
                text = k.value()
                text = text.split('">')[-1]
                text = text.split('</')[0]
                n['label'].setValue(str(text))
            elif l.value() == "center":
                text = k.value()
                text = text.split('">')[-1]
                text = text.split('</')[0]
                n['label'].setValue('<p style="text-align:center">' + str(text) + '</p>')
            else:
                text = k.value()
                text = text.split('">')[-1]
                text = text.split('</')[0]
                n['label'].setValue('<p style="text-align:right">' + str(text) + '</p>')
    
    
    bdScalePlus = '''
step = 50
nuke.thisNode()['xpos'].setValue(nuke.thisNode()['xpos'].getValue()-step)
nuke.thisNode()['ypos'].setValue(nuke.thisNode()['ypos'].getValue()-step)
nuke.thisNode()['bdheight'].setValue(nuke.thisNode()['bdheight'].getValue()+step*2)
nuke.thisNode()['bdwidth'].setValue(nuke.thisNode()['bdwidth'].getValue()+step*2)
'''
        
    bdScaleMin = '''
step = 50
#Check if scale is minimal value 
#If True don't scale smaller. 
if nuke.thisNode()['bdwidth'].value() <= 100 or nuke.thisNode()['bdheight'].value() <= 60:
    nuke.thisNode()['bdheight'].setValue(60)
    nuke.thisNode()['bdwidth'].setValue(100)

else:
    nuke.thisNode()['xpos'].setValue(nuke.thisNode()['xpos'].getValue()+step)
    nuke.thisNode()['ypos'].setValue(nuke.thisNode()['ypos'].getValue()+step)
    nuke.thisNode()['bdheight'].setValue(nuke.thisNode()['bdheight'].getValue()-step*2)
    nuke.thisNode()['bdwidth'].setValue(nuke.thisNode()['bdwidth'].getValue()-step*2)
'''

    
    
    ## create variables ##
    ## Label
    try: 
        backdorpLabel = backdrop['label']
        backdrop.addKnob(backdorpLabel)
    except:
        print('Label button already exist.')
        pass
    
    ## Font Size Slider
    fontSizeSlider = nuke.Double_Knob('fontSize', 'font size')
    minMax = ['1', '100']
    fontSizeSlider.setRange(10, 100)
    backdrop.addKnob(fontSizeSlider)
    fontSizeSlider.setValue(50)
    #nuke.addKnobChanged(font_size_code)
    
    
    ## Pulldown button text centers
    fontPlacementList = [ 'left', 'center', 'right' ] 
    fontPlacement = nuke.Enumeration_Knob('fontPlacement', '', fontPlacementList)
    fontPlacement.clearFlag(nuke.STARTLINE)
    fontPlacement.setFlag(nuke.ENDLINE)
    backdrop.addKnob(fontPlacement)
    
    ## Buttons Resize
    pyButtonPlus = nuke.PyScript_Knob('backdropScalePlus', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Plus.png'>")
    backdrop.addKnob(pyButtonPlus)
    pyButtonMin = nuke.PyScript_Knob('backdropScaleMin', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Min.png'>")
    backdrop.addKnob(pyButtonMin)
    
    # Buttons for preset colors
    # "<img src='./icons/GB_BackdropNode/GB_Red.png'>"
    #gb_red = "./icons/GB_BackdropNode/GB_Red.png"
    #backdrop['icon'].setValue("./icons/GB_BackdropNode/GB_Red.png")
    pyButtonRed = nuke.PyScript_Knob('backdropColorRed', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Red.png'>")
    backdrop.addKnob(pyButtonRed)
    setColorRed = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(2000633855)"
    backdrop['backdropColorRed'].setValue(setColorRed)
    
    pyButtonOrange = nuke.PyScript_Knob('backdropColorOrange', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Orange.png'>")
    backdrop.addKnob(pyButtonOrange)
    setColorOrange = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(2002796543)"
    backdrop['backdropColorOrange'].setValue(setColorOrange)
    
    pyButtonYellow = nuke.PyScript_Knob('backdropColorYellow', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Yellow.png'>")
    backdrop.addKnob(pyButtonYellow)
    setColorYellow = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(2004156671)"
    backdrop['backdropColorYellow'].setValue(setColorYellow)
    
    pyButtonLightGreen = nuke.PyScript_Knob('backdropColorLightGreen', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_LGreen.png'>")
    backdrop.addKnob(pyButtonLightGreen)
    setColorLightGreen = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(896991487)"
    backdrop['backdropColorLightGreen'].setValue(setColorLightGreen)
    
    pyButtonGreen = nuke.PyScript_Knob('backdropColorGreen', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Green.png'>")
    backdrop.addKnob(pyButtonGreen)
    setColorGreen = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(4456703)"
    backdrop['backdropColorGreen'].setValue(setColorGreen)
    #backdrop['icon'].setValue('./icons/GB_BackdropNode/GB_Red.png')
    
    pyButtonLightBlue = nuke.PyScript_Knob('backdropColorLightBlue', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_LBlue.png'>")
    backdrop.addKnob(pyButtonLightBlue)
    setColorLightBlue = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(7108607)"
    backdrop['backdropColorLightBlue'].setValue(setColorLightBlue)
    
    pyButtonBlue = nuke.PyScript_Knob('backdropColorBlue', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Blue.png'>")
    backdrop.addKnob(pyButtonBlue)
    setColorBlue = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(96255)"
    backdrop['backdropColorBlue'].setValue(setColorBlue)
    
    pyButtonPurple = nuke.PyScript_Knob('backdropColorPurple', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Purple.png'>")
    backdrop.addKnob(pyButtonPurple)
    setColorPurple = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(1325430783)"
    backdrop['backdropColorPurple'].setValue(setColorPurple)
    
    pyButtonPink = nuke.PyScript_Knob('backdropColorPink', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Pink.png'>")
    backdrop.addKnob(pyButtonPink)
    setColorPink = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(1996514559)"
    backdrop['backdropColorPink'].setValue(setColorPink)
    
    pyButtonGrey  = nuke.PyScript_Knob('backdropColorGrey', "<img src='C:/Users/The Compound PC 10/.nuke./icons/GB_BackdropNode/GB_Grey.png'>")
    backdrop.addKnob(pyButtonGrey)
    setColorGrey = "thisNode = nuke.thisNode()\nthisNode['tile_color'].setValue(1145324799)"
    backdrop['backdropColorGrey'].setValue(setColorGrey)
    
    
    #backdrop.removeKnob(pyButtonGrey)
    #backdrop.removeKnob(fontPlacement)
    
    ## Add values to added knobs
    backdrop['backdropScalePlus'].setValue(bdScalePlus)
    backdrop['backdropScaleMin'].setValue(bdScaleMin)
    
    ## Add Callback to "fontSizeSlider" and "fontPlacement".
    backdrop.knob('fontSizeSlider')
    nuke.addKnobChanged(font_size_code)
    
    ## control panel
    backdrop.showControlPanel(True)

nuke.addOnUserCreate(addButtons, nodeClass='BackdropNode')
