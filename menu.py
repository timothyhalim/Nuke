#
#
#  Timothy Halim Septianjaya
#  timo.ink
#
#

import os
import nuke

menu = nuke.menu('Nuke')
menu.addCommand( 'General/Create Read from Write', 'from Timo.self_made.Scripts import readFromWrite;readFromWrite.main()', 'ctrl+r' )
menu.addCommand( 'General/Write Read Explorer', 'from Timo.self_made.Scripts import fileExplorer;fileExplorer.main()', 'ctrl+e' )
menu.addCommand( 'General/Reload Read', 'from Timo.self_made.Scripts import reloadRead;reloadRead.main()', 'shift+r' )

menu.addCommand( 'General/Display Selected nodes property', 'from Timo.self_made.Scripts import displayProperties;displayProperties.main()', 'shift+d' )
menu.addCommand( 'General/Render Selected Nodes', 'from Timo.self_made.Scripts import renderNodes;renderNodes.showRenderDialog(nuke.selectedNodes())', 'alt+r' )
menu.addCommand( 'General/LGT Helper', 'from Timo.self_made.Scripts import LGTHelper;nukescripts.panels.registerWidgetAsPanel("LGTHelper.LGTHelper", "Timo.ink", "timo.ink.filebrowserWindow");pane = nuke.getPaneFor("Properties.1");nukescripts.panels.registerWidgetAsPanel("LGTHelper.LGTHelper", "Timo.ink", "timo.ink.filebrowserWindow", True).addToPane(pane)', 'ctrl+b' )

# LOAD ALL GIZMO IN GIZMO FOLDER
gizmodir = os.listdir( os.path.join( os.path.dirname(__file__), 'gizmos' ) )
gizmolist = [ x.split ( '.' )[0] for x in gizmodir if x.endswith ( 'gizmo' ) ]
for o in gizmolist:	
    toolbar = nuke.menu( 'Nodes' ).addMenu( 'Timo', icon='Timo.png' ).addCommand(str(o) )

# Gizmo Callbacks
from Timo.self_made.Scripts import projectControl
projectControl.projectControl_setup()