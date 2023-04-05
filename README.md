# backdropNodeButtons
Add preset buttons to the backdrop node. Makes it easiers to change to a preset color and adjusting the font size. Added a keyboard shortcut 'alt+b'.  

## info:
Inspired by Franklin with his F_Backdrop script. I recreated it for myself as a learning process. 
<img width="1016" alt="image" src="https://user-images.githubusercontent.com/105785047/230104534-b6f55178-3453-493a-b0da-d888784f6723.png">

## install
1. Put the file in your .nuke folder. 
2. Set the following in your menu.py file:

import GB_backdropNode

nukescripts.autoBackdrop = GB_backdropNode.backdropNode # Original backdrop function replacement

nuke.menu('Nodes').addCommand( 'Golan gizmos/Golan/backdropNode', 'GB_backdropNode.backdropNode()', 'alt+b')
